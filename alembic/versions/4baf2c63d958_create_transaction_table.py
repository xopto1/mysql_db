"""create transaction table

Revision ID: 4baf2c63d958
Revises: 006cf379ac80
Create Date: 2019-08-14 20:10:53.214149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4baf2c63d958'
down_revision = '006cf379ac80'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transaction',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('issued_at', sa.String(50), nullable=False),
        sa.Column('remote_addr', sa.DateTime(50), nullable=False),
    )


def downgrade():
    op.drop_table('transaction')
