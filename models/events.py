import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
# Needed for continuum
from sqlalchemy_continuum import make_versioned

# Needed for continuum
make_versioned(user_cls=None)
Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String())
    start_time = sa.Column(sa.DateTime, nullable=False)
    end_time = sa.Column(sa.DateTime, nullable=False)
    description = sa.Column(sa.Text)
    schedule_published_on = sa.Column(sa.DateTime)
