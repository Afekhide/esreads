"""edited User model

Revision ID: d612522a4756
Revises: 651c3528a641
Create Date: 2022-06-10 18:55:35.832758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd612522a4756'
down_revision = '651c3528a641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('Unique_api_key', ['api_key'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('Unique_api_key', type_='unique')

    # ### end Alembic commands ###