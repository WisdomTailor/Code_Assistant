import os
import logging
from alembic.config import Config
from alembic import command
from dotenv import load_dotenv

# Load environment variables from db.env
if not load_dotenv("src/db/database/db.env"):
    logging.error("Could not load environment variables from db.env")

# Access the environment variables
host = os.environ.get("POSTGRES_HOST", "localhost")
port = int(os.environ.get("POSTGRES_PORT", 5432))
database = os.environ.get("POSTGRES_DB", "postgres")
user = os.environ.get("POSTGRES_USER", "postgres")
password = os.environ.get("POSTGRES_PASSWORD", "postgres")

# Set the SQLAlchemy database URL
db_url = f"postgresql://{user}:{password}@localhost:{port}/{database}"

# Initialize the Alembic configuration
alembic_cfg = Config()

# Set the database URL in the Alembic configuration
alembic_cfg.set_main_option("sqlalchemy.url", db_url)
alembic_cfg.set_main_option("script_location", "src/db/database/migrations")

# Run the Alembic upgrade command
command.upgrade(alembic_cfg, "head")
