"""deleted status

Revision ID: a78cff960455
Revises: b0b7398d540f
Create Date: 2023-10-05 19:55:02.532542

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = 'a78cff960455'
down_revision: Union[str, None] = 'b0b7398d540f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###