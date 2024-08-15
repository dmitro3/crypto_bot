"""add referal_id column

Revision ID: 2bc4029b5310
Revises: eb8ef973374f
Create Date: 2024-08-09 02:47:31.032286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bc4029b5310'
down_revision: Union[str, None] = 'eb8ef973374f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('referrer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk__users__referrer_id__users'), 'users', 'users', ['referrer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk__users__referrer_id__users'), 'users', type_='foreignkey')
    op.drop_column('users', 'referrer_id')
    # ### end Alembic commands ###
