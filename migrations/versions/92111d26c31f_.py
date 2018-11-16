"""empty message

Revision ID: 92111d26c31f
Revises: 59682372feed
Create Date: 2018-11-15 14:01:25.379853

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '92111d26c31f'
down_revision = '59682372feed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=32), nullable=True),
    sa.Column('district', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Float(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('showname', sa.String(length=128), nullable=True),
    sa.Column('shownameen', sa.String(length=128), nullable=True),
    sa.Column('director', sa.String(length=64), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=32), nullable=True),
    sa.Column('openday', sa.Date(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=64), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cinema_resource')
    op.drop_table('movie_resource')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_resource',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('showname', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('shownameen', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('director', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('leadingRole', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('language', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('duration', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('screeningmodel', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('openday', sa.DATE(), nullable=True),
    sa.Column('backgroundpicture', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('flag', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('isdelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('cinema_resource',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('district', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('score', mysql.FLOAT(), nullable=True),
    sa.Column('hallnum', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('servicecharge', mysql.FLOAT(), nullable=True),
    sa.Column('astrict', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('flag', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('isdelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('movie')
    op.drop_table('cinema')
    # ### end Alembic commands ###