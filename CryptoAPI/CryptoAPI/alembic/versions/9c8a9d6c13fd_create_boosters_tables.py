"""create boosters tables

Revision ID: 9c8a9d6c13fd
Revises: 5e4f842c757b
Create Date: 2024-09-09 00:05:17.629339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c8a9d6c13fd'
down_revision: Union[str, None] = '5e4f842c757b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booster_effects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('booster_type', sa.Enum('RANGE', 'LEVERAGE', 'TRADES', name='boostertype'), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('effect_value', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__booster_effects'))
    )
    op.create_index(op.f('ix__booster_effects__id'), 'booster_effects', ['id'], unique=False)
    op.create_table('booster_prices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('booster_type', sa.Enum('RANGE', 'LEVERAGE', 'TRADES', name='boostertype'), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__booster_prices'))
    )
    op.create_index(op.f('ix__booster_prices__id'), 'booster_prices', ['id'], unique=False)
    op.create_table('boosters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('range_lvl', sa.Integer(), nullable=False),
    sa.Column('leverage_lvl', sa.Integer(), nullable=False),
    sa.Column('trades_lvl', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk__boosters__user_id__users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__boosters'))
    )
    op.create_index(op.f('ix__boosters__id'), 'boosters', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__boosters__id'), table_name='boosters')
    op.drop_table('boosters')
    op.drop_index(op.f('ix__booster_prices__id'), table_name='booster_prices')
    op.drop_table('booster_prices')
    op.drop_index(op.f('ix__booster_effects__id'), table_name='booster_effects')
    op.drop_table('booster_effects')
    # ### end Alembic commands ###
