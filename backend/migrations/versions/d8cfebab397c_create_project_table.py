"""create project table

Revision ID: d8cfebab397c
Revises: 4abdf7529663
Create Date: 2024-07-18 19:18:48.428730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8cfebab397c'
down_revision: Union[str, None] = '4abdf7529663'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=64), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("projects")