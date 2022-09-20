from models.settings import db
from datetime import datetime


class InvitationList(db.Model):
    __tablename__ = 'invitation_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_name = db.Column(db.String)
    list_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
