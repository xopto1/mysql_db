"""create users_version table

Revision ID: d1b1a9478695
Revises: 4baf2c63d958
Create Date: 2019-08-14 20:18:02.097704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1b1a9478695'
down_revision = '4baf2c63d958'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users_version',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('nickname', sa.String(50)),
        sa.Column('transaction_id', sa.Integer),
        sa.Column('end_transaction_id', sa.Integer),
        sa.Column('operation_type', sa.Integer),
    )


def downgrade():
    op.drop_table('users_version')
