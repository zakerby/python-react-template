"""Update project table add user_id

Revision ID: 0f4f89684113
Revises: d8cfebab397c
Create Date: 2024-07-30 11:51:48.099384

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f4f89684113'
down_revision: Union[str, None] = 'd8cfebab397c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('projects', sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False))


def downgrade() -> None:
    op.drop_column('projects', 'user_id')
