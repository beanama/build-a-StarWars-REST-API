"""empty message

Revision ID: 6964c2240219
Revises: e1ea122bf77b
Create Date: 2023-07-12 18:35:40.765138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6964c2240219'
down_revision = 'e1ea122bf77b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=True)

    with op.batch_alter_table('favourites', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=False)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('model',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=40),
               existing_nullable=False)
        batch_op.alter_column('starship_class',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('starship_class',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)
        batch_op.alter_column('model',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    with op.batch_alter_table('favourites', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=True)

    # ### end Alembic commands ###
