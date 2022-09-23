from models.settings import db
from datetime import datetime


class InvitationListItem(db.Model):
    __tablename__ = 'invitation_list_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_id = db.Column(db.Integer, db.ForeignKey('invitation_list.id'))
    list_member_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # database relationship  # noqa E501
    list_member = db.relationship("User")  # orm relationship
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               id,
               list_id,
               list_member_id,
               ):

        newInvListItem = self(id,
                              list_id=list_id,
                              list_member_id=list_member_id,
                              )
        db.add(newInvListItem)
        db.commit()
        return newInvListItem

    @classmethod
    def update(self,
               list_member_id=list_member_id,
               ):

        updateInvListItem = db.query(InvitationListItem) \
                            .filter_by(id=id).first()
        updateInvListItem.list_member_id = list_member_id
        updateInvListItem.updated_at = datetime.utcnow()

        db.add(updateInvListItem)
        db.commit()
        return updateInvListItem

    @classmethod
    def delete(self, id):
        deleteInvListItem = db.query(InvitationListItem) \
                            .filter_by(id=id).first()
        deleteInvListItem.deleted_at = datetime.utcnow()

        db.add(deleteInvListItem)
        db.commit()
        return deleteInvListItem
