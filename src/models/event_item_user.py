from models.settings import db
from datetime import datetime


class EventItemUser(db.Model):
    __tablename__ = 'event_item_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_item_id = db.Column(db.Integer, db.ForeignKey("event_item.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
