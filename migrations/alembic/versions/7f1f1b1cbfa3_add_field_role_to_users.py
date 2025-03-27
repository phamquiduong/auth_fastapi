"""Add field role to users

Revision ID: 7f1f1b1cbfa3
Revises: 0e764b486b4d
Create Date: 2025-03-28 01:41:04.193161

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '7f1f1b1cbfa3'
down_revision: Union[str, None] = '0e764b486b4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column('role', sa.String(16), nullable=False, default='guest', server_default='guest')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'role')
