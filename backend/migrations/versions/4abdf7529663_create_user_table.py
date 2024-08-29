"""create user table

Revision ID: 4abdf7529663
Revises: 
Create Date: 2024-07-18 19:16:58.229389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4abdf7529663'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("username", sa.String(length=64), nullable=False, unique=True),
        sa.Column("email", sa.String(length=80), nullable=False, unique=True),
        sa.Column("password", sa.String(length=500), nullable=False),
    )

def downgrade() -> None:
    op.drop_table("users")
