from models.all_models import User
from utils.database import create_db_session, connect_string


class UserRepository:
    def __init__(self):
        self.session = create_db_session(connect_string)

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()
        return obj

    def get(self, record_id):
        obj = self.session.query(User).get(record_id)
        return obj

    def update(self, obj):
        try:
            self.session.commit()
            self.session.refresh(obj)
            return obj
        except Exception as e:
            self.session.rollback()
            print(f'An Exception has occurred: {e}')
        return None

    def delete(self, obj):
        try:
            self.session.query(User).delete(obj.id)
            self.session.commit()
            return obj
        except Exception as e:
            self.session.rollback()
            print(f'An Exception has occurred: {e}')
        return None
