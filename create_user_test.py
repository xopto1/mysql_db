from models.all_models import User
from utils.database import create_db_session, connect_string

session = create_db_session(connect_string)


def create_user(user_obj):
    user = User(
        first_name=user_obj.first_name,
        last_name=user_obj.last_name,
        nickname=user_obj.nickname
    )
    session.add(user)
    session.commit()
    return user


def get_by_id(record_id):
    result = session.query(User).get(record_id)
    session.close()
    return result


def update_user(user_obj):
    record_to_update = get_by_id(user_obj.id)
    record_to_update.first_name = user_obj.first_name
    record_to_update.last_name = user_obj.last_name
    record_to_update.nickname = user_obj.nickname
    session.query(User).update(record_to_update)
    # persist to DB
    session.commit()

    return get_by_id(record_to_update.id)


# new_User = User(
#     first_name='A',
#     last_name='B',
#     nickname='Me too'
# )

update_record = User(
    id=2,
    first_name='',
    last_name='',
    nickname='Me too'
)

print(update_record.id)

updates = update_user(update_record)

# result = create_user(new_User)

print(f'This is the update result {updates}')
