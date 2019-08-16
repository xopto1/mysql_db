import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, orm
from sqlalchemy.ext.declarative import declarative_base
# Needed for continuum
from sqlalchemy_continuum import make_versioned

# Needed for continuum
make_versioned(user_cls=None)
Base = declarative_base()


class User(Base):
    # Needed for continuum
    __versioned__ = {}
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', nickname='%s')>" % (
                            self.first_name, self.last_name, self.nickname)


class Article(Base):
    __versioned__ = {}
    __tablename__ = 'article'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)

    def __repr__(self):
        return "<Article(name='%s', content='%s')>" % (
                            self.name, self.content)


class Event(Base):
    __versioned__ = {}
    __tablename__ = 'events'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String())
    start_time = sa.Column(sa.DateTime, nullable=False)
    end_time = sa.Column(sa.DateTime, nullable=False)
    description = sa.Column(sa.Text)
    schedule_published_on = sa.Column(sa.DateTime)

    def __repr__(self):
        return "<Event(name='%s', start_time='%s', end_time='%s', " \
               "description='%s', schedule_published_on='%s')>" % \
               (self.name, self.start_time, self.end_time, self.description,
                self.schedule_published_on)


# Needed for Continuum
sa.orm.configure_mappers()
