import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy_continuum import make_versioned
from sqlalchemy.ext.declarative import declarative_base

from utils.database import create_db_session, connect_string

make_versioned(user_cls=None)
Base = declarative_base()

session = create_db_session(connect_string)


class Article(Base):
    __versioned__ = {}
    __tablename__ = 'articles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)


# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()


article = Article(name=u'Some article', content='The content')
session.add(article)
session.commit()

article.versions[0].name == u'Some article'

article.name = u'Some updated article'

session.commit()

article.versions[1].name == u'Some updated article'