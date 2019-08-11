from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect_string = 'sqlite:///:memory:'
connect_string = 'mysql+pymysql://root:@localhost/sample_db_local'


def create_db_session(cs=connect_string):
    # TODO: Enable if you want VERBOSE sql statements generated
    # engine = create_engine(connect_string, echo=True)
    engine = create_engine(cs)
    SESSION = sessionmaker(bind=engine)
    session = SESSION()

    return session
