from models.settings import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_name = db.Column(db.String)
    event_start_date = db.Column(db.DateTime)
    event_end_date = db.Column(db.DateTime)
    event_time_hour_start = db.Column(db.Integer)
    event_time_minutes_start = db.Column(db.Integer)
    event_duration_minutes = db.Column(db.Integer)
    event_recurrence_period = db.Column(db.String)   # use crontab syntax
    send_event_invite_before_days = db.Column(db.Integer)
    send_event_invite_at_hour = db.Column(db.Integer)
    event_remind_before_hours = db.Column(db.Integer)
    invitation_list_id = db.Column(db.Integer,
                                   db.ForeignKey('invitation_list.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
