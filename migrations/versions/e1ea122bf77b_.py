"""empty message

Revision ID: e1ea122bf77b
Revises: 679493f6ef31
Create Date: 2023-07-12 18:30:51.933821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ea122bf77b'
down_revision = '679493f6ef31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('model', sa.String(length=15), nullable=False),
    sa.Column('starship_class', sa.String(length=15), nullable=False),
    sa.Column('crew', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    op.drop_table('favourites')
    # ### end Alembic commands ###
