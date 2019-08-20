from models.all_models import User
from repos.user import UserRepository

user_repo = UserRepository()

new_user = User(
    first_name='Another',
    last_name='User',
    nickname='A'
)


update_user = User(
    id=1,
    first_name='DDD',
    last_name='EEE',
    nickname='B'
)


def insert(obj):
    result = user_repo.create(obj)
    return result


def retrieve(record_id):
    result = user_repo.get(record_id)

    return result


def update(obj):
    result = user_repo.get(obj.id)
    result.first_name = obj.first_name

    user_repo.update(result)
    return obj


new_record = insert(new_user)
print(f'this is the new_record: {new_record}')

record = update(update_user)
print(f'this is the record: {record}')

# record = insert(new_user)
# print(f'this is the record: {record}')
#
# my_record = retrieve(record.id)
# print(f'this is the record: {my_record}')
