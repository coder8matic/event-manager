from models.settings import db
from datetime import datetime


class EventItem(db.Model):
    __tablename__ = 'event_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_item_name = db.Column(db.String)
    event_item_start_time = db.Column(db.DateTime)
    event_item_end_time = db.Column(db.DateTime)
    send_invite_time = db.Column(db.DateTime)
    send_reminder_time = db.Column(db.DateTime)
    invitation_list_id = db.Column(db.Integer,
                                   db.ForeignKey('invitation_list.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
