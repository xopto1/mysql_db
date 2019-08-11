"""create articles table

Revision ID: a34f924503cd
Revises: 90044b82f403
Create Date: 2019-08-11 14:38:39.610552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a34f924503cd'
down_revision = '90044b82f403'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.Unicode(255), nullable=False),
        sa.Column('content', sa.UnicodeText(), nullable=False)
    )


def downgrade():
    op.drop_table('articles')
