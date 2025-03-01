"""Add user notifications

Revision ID: 787a3b7301a7
Revises: d836bbe774c7
Create Date: 2025-03-01 22:00:12.220448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '787a3b7301a7'
down_revision: Union[str, None] = 'd836bbe774c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_notifications",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("message", sa.String(length=500)),
        sa.Column("is_read", sa.Boolean(), default=False),
    )


def downgrade() -> None:
    op.drop_table("users_notifications")