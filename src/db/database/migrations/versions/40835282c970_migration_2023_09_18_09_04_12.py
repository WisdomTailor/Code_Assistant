"""migration 2023-09-18_09-04-12

Revision ID: 40835282c970
Revises: 47b71d943f97
Create Date: 2023-09-18 09:04:13.057041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40835282c970'
down_revision = '47b71d943f97'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('additional_design_inputs', sa.Column('requirement_id', sa.Integer(), nullable=False))
    op.add_column('additional_design_inputs', sa.Column('description', sa.String(), nullable=False))
    op.drop_constraint('additional_design_inputs_requirements_id_fkey', 'additional_design_inputs', type_='foreignkey')
    op.create_foreign_key(None, 'additional_design_inputs', 'requirements', ['requirement_id'], ['id'])
    op.drop_column('additional_design_inputs', 'requirements_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('additional_design_inputs', sa.Column('requirements_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'additional_design_inputs', type_='foreignkey')
    op.create_foreign_key('additional_design_inputs_requirements_id_fkey', 'additional_design_inputs', 'requirements', ['requirements_id'], ['id'])
    op.drop_column('additional_design_inputs', 'description')
    op.drop_column('additional_design_inputs', 'requirement_id')
    # ### end Alembic commands ###
