"""added relation to table to order

Revision ID: 4cb0a8792fa8
Revises: eff25a5b8ce5
Create Date: 2023-10-05 18:20:48.402233

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = '4cb0a8792fa8'
down_revision: Union[str, None] = 'eff25a5b8ce5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###