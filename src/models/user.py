from src.db import getUser, getUserId

class UserModel():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        row = getUser(username)

        if row:
            user = cls(*row)
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):
        row = getUserId(_id)

        if row:
            user = cls(*row)
        else:
            user = None

        return user