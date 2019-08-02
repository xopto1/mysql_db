from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.all_models import User

# connect_string = 'sqlite:///:memory:'
connect_string = 'mysql+pymysql://root:@localhost/sample_db_local'
engine = create_engine(connect_string, echo=True)

SESSION = sessionmaker(bind=engine)
session = SESSION()


def create_user_direct():
    user = User(
        first_name='Kevin',
        last_name='McGonigal',
        nickname='Mr. Stark'
    )

    session.add(user)
    session.commit()


create_user_direct()
