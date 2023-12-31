"""refactor added date

Revision ID: 6b8e58f615ef
Revises: fed99fdc27c1
Create Date: 2023-10-05 15:25:11.165157

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = '6b8e58f615ef'
down_revision: Union[str, None] = 'fed99fdc27c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'date')
    # ### end Alembic commands ###
