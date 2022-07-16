"""added column

Revision ID: 651c3528a641
Revises: 183e794ccc26
Create Date: 2022-06-10 05:08:16.841341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651c3528a641'
down_revision = '183e794ccc26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True, default=0))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Role', schema=None) as batch_op:
        batch_op.drop_column('default')

    # ### end Alembic commands ###
