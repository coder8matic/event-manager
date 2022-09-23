from models.settings import db
from datetime import datetime


class InvitationList(db.Model):
    __tablename__ = 'invitation_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_name = db.Column(db.String)
    list_owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # database relationship  # noqa E501
    list_owner = db.relationship("User")  # orm relationship
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               list_name,
               list_owner_id,
               ):

        newInvList = self(list_name=list_name,
                          list_owner_id=list_owner_id,
                          )
        db.add(newInvList)
        db.commit()
        return newInvList

    @classmethod
    def update(self,
               id,
               list_name,
               list_owner_id,
               ):

        updateInvList = db.query(InvitationList).filter_by(id=id).first()
        updateInvList.list_name = list_name
        updateInvList.list_owner_id = list_owner_id
        updateInvList.updated_at = datetime.utcnow()

        db.add(updateInvList)
        db.commit()
        return updateInvList

    @classmethod
    def delete(self, id):
        deleteInvList = db.query(InvitationList).filter_by(id=id).first()
        deleteInvList.deleted_at = datetime.utcnow()

        db.add(deleteInvList)
        db.commit()
        return deleteInvList
