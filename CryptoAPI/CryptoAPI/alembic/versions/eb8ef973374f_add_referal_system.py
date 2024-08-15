"""add referal system

Revision ID: eb8ef973374f
Revises: 11111099d8ad
Create Date: 2024-08-09 01:49:01.371719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'eb8ef973374f'
down_revision: Union[str, None] = '11111099d8ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('referrals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('referrer_id', sa.Integer(), nullable=False),
    sa.Column('referred_id', sa.Integer(), nullable=False),
    sa.Column('is_premium', sa.Boolean(), nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['referred_id'], ['users.id'], name=op.f('fk__referrals__referred_id__users')),
    sa.ForeignKeyConstraint(['referrer_id'], ['users.id'], name=op.f('fk__referrals__referrer_id__users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__referrals'))
    )
    op.create_index(op.f('ix__referrals__id'), 'referrals', ['id'], unique=False)
    op.add_column('users', sa.Column('referral_code', sa.String(), nullable=True))
    op.create_unique_constraint(op.f('uq__users__referral_code'), 'users', ['referral_code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__users__referral_code'), 'users', type_='unique')
    op.drop_column('users', 'referral_code')
    op.drop_index(op.f('ix__referrals__id'), table_name='referrals')
    op.drop_table('referrals')
    # ### end Alembic commands ###
