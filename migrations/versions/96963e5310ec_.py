"""empty message

Revision ID: 96963e5310ec
Revises: 
Create Date: 2018-11-14 04:10:49.913713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96963e5310ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email2', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'users', ['email2'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email2')
    # ### end Alembic commands ###
