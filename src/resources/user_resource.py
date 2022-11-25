from src import db
from src.models.user import SystemUser


class UserResource:
    def __int__(self):
        pass

    @staticmethod
    def search_user_by_username(username):
        return db.session.query(SystemUser).filter_by(username=username).first()

    @staticmethod
    def search_user_by_email(email):
        return db.session.query(SystemUser).filter_by(email=email).first()

    @staticmethod
    def search_user_by_phone(phone):
        return db.session.query(SystemUser).filter_by(phone=phone).first()

    @staticmethod
    def get_password(email):
        return db.session.query(SystemUser.password).filter_by(email=email).first()[0]

    @staticmethod
    def save_user(username, email, phone, password):
        user = SystemUser(username=username, email=email, phone=phone, password=password)
        db.session.add(user)
        db.session.commit()
