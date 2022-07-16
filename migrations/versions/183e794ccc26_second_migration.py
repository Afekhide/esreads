"""second migration

Revision ID: 183e794ccc26
Revises: 8fcfe27de82c
Create Date: 2022-06-10 04:58:17.490971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183e794ccc26'
down_revision = '8fcfe27de82c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=False, default=0))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Role', schema=None) as batch_op:
        batch_op.drop_column('default')

    # ### end Alembic commands ###