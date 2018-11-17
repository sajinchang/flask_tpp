"""empty message

Revision ID: 5b69f6e379e0
Revises: 0b6948e2a963
Create Date: 2018-11-17 14:18:18.797141

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b69f6e379e0'
down_revision = '0b6948e2a963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'order_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('order_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
