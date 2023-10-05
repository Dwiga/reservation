"""refactor remove day

Revision ID: fed99fdc27c1
Revises: 57453085e215
Create Date: 2023-10-05 15:24:30.586709

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = 'fed99fdc27c1'
down_revision: Union[str, None] = '57453085e215'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'day')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('day', sa.DATE(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###