from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect_string = 'sqlite:///:memory:'
connect_string = 'mysql+pymysql://root:@localhost/sample_db_local'


def create_db_session(connect_string):
    engine = create_engine(connect_string, echo=True)
    SESSION = sessionmaker(bind=engine)
    session = SESSION()

    return session
