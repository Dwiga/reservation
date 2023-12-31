"""added token to user

Revision ID: 25d99840431c
Revises: 28f2bfa067db
Create Date: 2023-10-05 08:43:46.147608

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from typing import Union, Sequence


# revision identifiers, used by Alembic.
revision: str = '25d99840431c'
down_revision: Union[str, None] = '28f2bfa067db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token')
    # ### end Alembic commands ###
