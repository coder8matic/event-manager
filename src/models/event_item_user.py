from models.settings import db
from datetime import datetime


class EventItemUser(db.Model):
    __tablename__ = 'event_item_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_item_id = db.Column(db.Integer, db.ForeignKey("event_item.id"))
    event_item = db.relationship("EventItem",)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # database relationship  # noqa E501
    user = db.relationship("User")  # orm relationship
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               event_item_id,
               user_id,
               ):

        newEventItemUser = self(event_item_id=event_item_id,
                                user_id=user_id,
                                )
        db.add(newEventItemUser)
        db.commit()
        return newEventItemUser

    @classmethod
    def update(self,
               id,
               event_item_id,
               user_id,
               ):

        updateEventItemUser = db.query(EventItemUser).filter_by(id=id).first()
        updateEventItemUser.event_item_id = event_item_id,
        updateEventItemUser.user_id = user_id,
        updateEventItemUser.updated_at = datetime.utcnow()

        db.add(updateEventItemUser)
        db.commit()
        return updateEventItemUser

    @classmethod
    def delete(self, id):
        deleteEventItem = db.query(EventItemUser).filter_by(id=id).first()
        deleteEventItem.deleted_at = datetime.utcnow()

        db.add(deleteEventItem)
        db.commit()
        return deleteEventItem
