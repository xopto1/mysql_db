import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_continuum import make_versioned

from utils.database import create_db_session, connect_string

session = create_db_session(connect_string)
Base = declarative_base()
make_versioned(user_cls=None)


class Article(Base):
    __versioned__ = {}
    __tablename__ = 'article'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)


article = Article(name='Some article', content='Some content')
session.add(article)
session.commit()

# article has now one version stored in database
article.versions[0].name
# 'Some article'

article.name = 'Updated name'
session.commit()

article.versions[1].name
# 'Updated name'


# lets revert back to first version
article.versions[0].revert()

article.name
# 'Some article'