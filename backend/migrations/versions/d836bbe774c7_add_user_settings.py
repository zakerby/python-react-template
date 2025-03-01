"""Add user settings

Revision ID: d836bbe774c7
Revises: 0f4f89684113
Create Date: 2025-03-01 18:59:37.870424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd836bbe774c7'
down_revision: Union[str, None] = '0f4f89684113'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_settings",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("first_name", sa.String(length=64)),
        sa.Column("last_name", sa.String(length=64)),
        sa.Column("email", sa.String(length=80)),
        sa.Column("phone_number", sa.String(length=15)),
        sa.Column("bio", sa.String(length=500)),
        sa.Column("profile_picture", sa.String(length=500)),
        sa.Column("theme", sa.String(length=64)),
    )

def downgrade() -> None:
    op.drop_table("users_settings")
