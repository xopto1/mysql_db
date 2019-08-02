"""create users table

Revision ID: 90044b82f403
Revises: 
Create Date: 2019-08-01 20:31:08.679758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90044b82f403'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('nickname', sa.String(50), nullable=True),
    )


def downgrade():
    op.drop_table('users')
