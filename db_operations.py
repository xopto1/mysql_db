from models.all_models import User
from repos.user import UserRepository

user_repo = UserRepository()

# insert_record = User(
#     first_name='First',
#     last_name='Last',
#     nickname='Nickname'
# )

record = user_repo.get(9)

delete = user_repo.delete(record)
print(f'This is the result of the delete: {delete}')
#
# record.first_name = 'Updated_First_Name'
#
# update_result = user_repo.update(record)
#
# print(f'This is the updated record: {update_result}')
#
# update_result = user_repo.update(insert_result)
#
# print(f'This is the updated record: {update_result}')
#
#
