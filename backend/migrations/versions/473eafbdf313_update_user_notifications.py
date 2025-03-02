"""Update user notifications

Revision ID: 473eafbdf313
Revises: 787a3b7301a7
Create Date: 2025-03-02 15:40:00.219666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '473eafbdf313'
down_revision: Union[str, None] = '787a3b7301a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users_notifications', sa.Column('title', sa.String(length=64), nullable=False))

def downgrade() -> None:
    op.drop_column('users_notifications', 'title')