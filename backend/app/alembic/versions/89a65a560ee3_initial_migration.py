"""Initial migration

Revision ID: 89a65a560ee3
Revises: 902f6290a3b7
Create Date: 2024-07-14 02:06:11.396820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89a65a560ee3'
down_revision: Union[str, None] = '902f6290a3b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companymedia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('media_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['media_id'], ['media.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companymedia')
    op.drop_table('media')
    # ### end Alembic commands ###
