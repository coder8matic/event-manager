from models.settings import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    email_verified = db.Column(db.Boolean, default=False)
    email_verified_code = db.Column(db.String, default=None)
    email_verified_code_valid_to = db.Column(db.DateTime, default=None)
    password = db.Column(db.String)
    password_reset_token = db.Column(db.String, default=None)
    password_reset_token_valid_to = db.Column(db.DateTime, default=None)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               email,
               password,
               ):

        newUser = self(email=email,
                       password=password,
                       )
        print("newUser.__dict__")
        print(newUser.__dict__)
        db.add(newUser)
        db.commit()
        return newUser

    @classmethod
    def update(self,
               id,
               email,
               email_verified,
               email_verified_code,
               email_verified_code_valid_to,
               password,
               password_reset_token,
               password_reset_token_valid_to,
               ):

        updateUser = db.query(User).filter_by(id=id).first()
        updateUser.email = email,
        updateUser.email_verified = email_verified,
        updateUser.email_verified_code = email_verified_code,
        updateUser.email_verified_code_valid_to = email_verified_code_valid_to,
        updateUser.password = password,
        updateUser.password_reset_token = password_reset_token,
        updateUser.password_reset_token_valid_to = password_reset_token_valid_to,  # noqa E501
        updateUser.updated_at = datetime.utcnow()

        db.add(updateUser)
        db.commit()
        return updateUser

    @classmethod
    def delete(self, id):
        deleteUser = db.query(User).filter_by(id=id).first()
        deleteUser.deleted_at = datetime.utcnow()

        db.add(deleteUser)
        db.commit()
        return deleteUser
