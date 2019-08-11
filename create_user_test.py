from models.all_models import User
from utils.database import create_db_session, connect_string

session = create_db_session(connect_string)


def create_user_direct():
    user = User(
        first_name='Adam',
        last_name='Jensen',
        nickname='Augmented1'
    )

    session.add(user)
    session.commit()


create_user_direct()
