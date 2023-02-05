from flask_login import UserMixin

from app.database import ReadDataBase


class UserLogin(UserMixin):
    def from_db(self, user_id, db):
        self.__user = ReadDataBase.get_user_by_id(db, user_id)[0]
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.id)
