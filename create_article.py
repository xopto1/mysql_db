from models.all_models import Article
from utils.database import create_db_session, connect_string

session = create_db_session(connect_string)


def create_record():
    article = Article(
        name='Article One',
        content='Blah. Yap, yap',
    )

    session.add(article)
    session.commit()


create_record()
