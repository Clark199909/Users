from src import db


class SystemUser(db.Model):
    __tablename__ = 'system_user'

    username = db.Column(db.String(50), primary_key=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

