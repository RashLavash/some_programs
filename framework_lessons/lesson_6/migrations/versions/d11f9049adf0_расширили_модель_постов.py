"""Расширили модель постов

Revision ID: d11f9049adf0
Revises: 36ee656fe0f6
Create Date: 2023-12-02 20:46:19.686745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd11f9049adf0'
down_revision = '36ee656fe0f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('data')

    # ### end Alembic commands ###
