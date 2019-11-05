"""create articles_version table

Revision ID: e2919cec02ab
Revises: d1b1a9478695
Create Date: 2019-11-05 12:14:56.687750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2919cec02ab'
down_revision = 'd1b1a9478695'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'articles_version',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.Unicode(255), nullable=False),
        sa.Column('content', sa.UnicodeText(), nullable=False),
        sa.Column('transaction_id', sa.Integer, nullable=False),
        sa.Column('end_transaction_id', sa.Integer, nullable=True),
        sa.Column('operation_type', sa.Integer, nullable=True)
    )


def downgrade():
    op.drop_table('articles_version')

