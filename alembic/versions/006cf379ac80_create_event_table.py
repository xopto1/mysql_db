"""create event table

Revision ID: 006cf379ac80
Revises: a34f924503cd
Create Date: 2019-08-11 14:57:49.846211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006cf379ac80'
down_revision = 'a34f924503cd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String()),
        sa.Column('start_time', sa.DateTime, nullable=False),
        sa.Column('end_time', sa.DateTime, nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('schedule_published_on', sa.DateTime)
    )


def downgrade():
    op.drop_table('events')
