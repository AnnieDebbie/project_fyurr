"""empty message

Revision ID: a4ebe8f13267
Revises: 657c546d4743
Create Date: 2022-08-25 15:26:04.113624

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a4ebe8f13267'
down_revision = '657c546d4743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'genres')
    op.drop_column('venues', 'genres')
    op.drop_column('venues', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('test', postgresql.ARRAY(sa.VARCHAR(length=120)), autoincrement=False, nullable=True))
    op.add_column('venues', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
