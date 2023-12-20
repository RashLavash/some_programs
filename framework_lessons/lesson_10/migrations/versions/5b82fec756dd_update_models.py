"""update models

Revision ID: 5b82fec756dd
Revises: 
Create Date: 2023-12-16 19:50:26.127409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b82fec756dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tag',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag_name', sa.Text(), nullable=False))
        batch_op.drop_column('post_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_name', sa.TEXT(), nullable=False))
        batch_op.drop_column('tag_name')

    op.drop_table('post_tag')
    # ### end Alembic commands ###
