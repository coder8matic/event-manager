from models.settings import db
from datetime import datetime


class EventItem(db.Model):
    __tablename__ = 'event_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_item_name = db.Column(db.String)
    event_item_invitation_text = db.Column(db.String)
    event_item_start_time = db.Column(db.DateTime)
    event_item_end_time = db.Column(db.DateTime)
    send_invite_time = db.Column(db.DateTime)
    send_reminder_time = db.Column(db.DateTime)
    invitation_list_id = db.Column(db.Integer,
                                   db.ForeignKey('invitation_list.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               event_id,
               event_item_name,
               event_item_invitation_text,
               event_item_start_time,
               event_item_end_time,
               send_invite_time,
               send_reminder_time,
               invitation_list_id,
               ):

        newEventItem = self(event_id=event_id,
                            event_item_name=event_item_name,
                            event_item_invitation_text=event_item_invitation_text,  # noqa E501
                            event_item_start_time=event_item_start_time,
                            event_item_end_time=event_item_end_time,
                            send_invite_time=send_invite_time,
                            send_reminder_time=send_reminder_time,
                            invitation_list_id=invitation_list_id,
                            )
        db.add(newEventItem)
        db.commit()
        return newEventItem

    @classmethod
    def update(self,
               id,
               event_id,
               event_item_name,
               event_item_invitation_text,
               event_item_start_time,
               event_item_end_time,
               send_invite_time,
               send_reminder_time,
               invitation_list_id,
               ):

        updateEventItem = db.query(EventItem).filter_by(id=id).first()
        updateEventItem.event_id = event_id,
        updateEventItem.event_item_name = event_item_name,
        updateEventItem.event_item_invitation_text = event_item_invitation_text,  # noqa E501
        updateEventItem.event_item_start_time = event_item_start_time,
        updateEventItem.event_item_end_time = event_item_end_time,
        updateEventItem.send_invite_time = send_invite_time,
        updateEventItem.send_reminder_time = send_reminder_time,
        updateEventItem.invitation_list_id = invitation_list_id,
        updateEventItem.updated_at = datetime.utcnow()

        db.add(updateEventItem)
        db.commit()
        return updateEventItem

    @classmethod
    def delete(self, id):
        deleteEventItem = db.query(EventItem).filter_by(id=id).first()
        deleteEventItem.deleted_at = datetime.utcnow()

        db.add(deleteEventItem)
        db.commit()
        return deleteEventItem
