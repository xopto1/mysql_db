from models.all_models import User
from repos.user import UserRepository

user_repo = UserRepository()

new_user = User(
    first_name='New',
    last_name='User',
    nickname='A'
)


def insert(obj):
    insert_result = user_repo.create(obj)
    print(f'This is the result of the insert: {insert_result}')


def retrieve(record_id):
    result = user_repo.get(record_id)

    return result


my_record = retrieve(10)
print(my_record)
