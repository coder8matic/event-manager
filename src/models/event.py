from models.settings import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_host_id = db.Column(db.Integer, db.ForeignKey('user.id')) # database relationship # noqa E501
    event_host = db.relationship('User')  # orm relationship  # noqa E501
    event_name = db.Column(db.String)
    event_invitation_text = db.Column(db.String, default=None)
    event_start_date = db.Column(db.String)
    event_end_date = db.Column(db.String)
    event_time_start = db.Column(db.String)
    event_duration_minutes = db.Column(db.Integer)
    event_recurrence_period = db.Column(db.String)   # use crontab syntax
    send_event_invite_before_days = db.Column(db.Integer)
    send_event_invite_at_hour = db.Column(db.Integer)
    event_remind_before_hours = db.Column(db.Integer)
    invitation_list_id = db.Column(db.Integer,
                                   db.ForeignKey('invitation_list.id'))  # database relationship # noqa E501
    invitation_list = db.relationship("InvitationList")  # orm relationship  # noqa E501
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               event_host_id,
               event_name,
               event_invitation_text,
               event_start_date,
               event_end_date,
               event_time_start,
               event_duration_minutes,
               event_recurrence_period,
               send_event_invite_before_days,
               send_event_invite_at_hour,
               event_remind_before_hours,
               invitation_list_id):

        newEvent = self(event_host_id=event_host_id,
                        event_name=event_name,
                        event_invitation_text=event_invitation_text,
                        event_start_date=event_start_date,
                        event_end_date=event_end_date,
                        event_time_start=event_time_start,
                        event_duration_minutes=event_duration_minutes,
                        event_recurrence_period=event_recurrence_period,
                        send_event_invite_before_days=send_event_invite_before_days,  # noqa E501
                        send_event_invite_at_hour=send_event_invite_at_hour,
                        event_remind_before_hours=event_remind_before_hours,
                        invitation_list_id=invitation_list_id,
                        )
        db.add(newEvent)
        db.commit()
        return newEvent

    @classmethod
    def update(self,
               id,
               event_host_id,
               event_name,
               event_invitation_text,
               event_start_date,
               event_end_date,
               event_time_start,
               event_duration_minutes,
               event_recurrence_period,
               send_event_invite_before_days,
               send_event_invite_at_hour,
               event_remind_before_hours,
               invitation_list_id):

        updateEvent = db.query(Event).filter_by(id=id).first()
        updateEvent.event_host_id = event_host_id
        updateEvent.event_name = event_name
        updateEvent.event_invitation_text = event_invitation_text
        updateEvent.event_start_date = event_start_date
        updateEvent.event_end_date = event_end_date
        updateEvent.event_time_start = event_time_start
        updateEvent.event_duration_minutes = event_duration_minutes
        updateEvent.event_recurrence_period = event_recurrence_period
        updateEvent.send_event_invite_before_days = send_event_invite_before_days  # noqa E501
        updateEvent.send_event_invite_at_hour = send_event_invite_at_hour
        updateEvent.event_remind_before_hours = event_remind_before_hours
        updateEvent.invitation_list_id = invitation_list_id
        updateEvent.updated_at = datetime.utcnow()

        db.add(updateEvent)
        db.commit()
        return updateEvent

    @classmethod
    def delete(self, id):
        deleteEvent = db.query(Event).filter_by(id=id).first()
        deleteEvent.deleted_at = datetime.utcnow()

        db.add(deleteEvent)
        db.commit()
        return deleteEvent
