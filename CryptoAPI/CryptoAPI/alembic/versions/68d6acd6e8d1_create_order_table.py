"""create order table

Revision ID: 68d6acd6e8d1
Revises: b01460841edc
Create Date: 2024-08-22 05:29:57.946305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68d6acd6e8d1'
down_revision: Union[str, None] = 'b01460841edc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
