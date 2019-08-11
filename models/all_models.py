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
                            self.full_name, self.last_name, self.nickname)


class Article(Base):
    __versioned__ = {}
    __tablename__ = 'article'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)


# Needed for Continuum
sa.orm.configure_mappers()
