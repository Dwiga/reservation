"""refactor time

Revision ID: 57453085e215
Revises: 8916ab248cd4
Create Date: 2023-10-05 10:56:26.330397

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = '57453085e215'
down_revision: Union[str, None] = '8916ab248cd4'
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