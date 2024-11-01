""" add task is_complete

Revision ID: 0b2525e4c21e
Revises: 512d457d8e4e
Create Date: 2024-11-01 18:54:15.127417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2525e4c21e'
down_revision = '512d457d8e4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list_api_development', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_complete', sa.Boolean(), nullable=False, server_default='f'))
        

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list_api_development', schema=None) as batch_op:
        batch_op.drop_column('is_complete')

    # ### end Alembic commands ###
