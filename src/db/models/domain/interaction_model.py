from db.database.models import Interaction

class InteractionModel:
    def __init__(self, id, record_created, interaction_summary, needs_summary, user_id, is_deleted,
                 conversations=None):
        self.id = id
        self.record_created = record_created
        self.interaction_summary = interaction_summary
        self.needs_summary = needs_summary
        self.user_id = user_id
        self.is_deleted = is_deleted
        self.conversations = conversations or []

    def to_database_model(self):
        return Interaction(
            id=self.id,
            record_created=self.record_created,
            interaction_summary=self.interaction_summary,
            needs_summary=self.needs_summary,
            user_id=self.user_id,
            is_deleted=self.is_deleted,
            conversations=self.conversations
        )

    @classmethod
    def from_database_model(cls, db_interaction):
        return cls(
            id=db_interaction.id,
            record_created=db_interaction.record_created,
            interaction_summary=db_interaction.interaction_summary,
            needs_summary=db_interaction.needs_summary,
            user_id=db_interaction.user_id,
            is_deleted=db_interaction.is_deleted,
            conversations=db_interaction.conversations
        )
