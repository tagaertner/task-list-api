"""empty message

Revision ID: 0ed5e811be21
Revises: 0b2525e4c21e
Create Date: 2024-11-04 21:46:02.425355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed5e811be21'
down_revision = '0b2525e4c21e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list_api_development', schema=None) as batch_op:
        batch_op.alter_column('is_complete',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list_api_development', schema=None) as batch_op:
        batch_op.alter_column('is_complete',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))

    # ### end Alembic commands ###