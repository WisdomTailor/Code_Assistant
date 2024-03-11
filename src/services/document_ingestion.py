from fastapi import APIRouter, UploadFile, File
from typing import List

from tasks.documents.document_ingestion_tasks import process_document_task

router = APIRouter()

@router.get("/test")
async def test():
    return {"message": "Hello World"}


@router.post("/ingest")
async def ingest_documents(
    active_collection_id:int,
    overwrite_existing_files:bool,
    split_documents:bool,
    create_summary_and_chunk_questions:bool,
    summarize_document:bool,
    chunk_size:int,
    chunk_overlap:int,
    files: List[UploadFile] = File(...),
):
    for file in files:
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        # Hand off to Celery for processing
        process_document_task.delay(file_location)

    return {"message": "Documents are being processed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(router, host="0.0.0.0", port=8000)