from models.settings import db
from datetime import datetime


class InvitationListMember(db.Model):
    __tablename__ = 'invitation_list_member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_id = db.Column(db.Integer, db.ForeignKey('invitation_list.id'))  # database relationship  # noqa E501
    list = db.relationship("InvitationList")  # orm relationship
    list_member_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # database relationship  # noqa E501
    list_member = db.relationship("User")  # orm relationship
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def create(self,
               list_id,
               list_member_id,
               ):

        newInvListMember = self(list_id=list_id,
                                list_member_id=list_member_id,
                                )
        db.add(newInvListMember)
        db.commit()
        return newInvListMember

    @classmethod
    def delete(self, id):
        deleteInvListMember = db.query(InvitationListMember) \
                            .filter_by(id=id) \
                            .filter_by(deleted_at=None).first()
        deleteInvListMember.deleted_at = datetime.utcnow()

        db.add(deleteInvListMember)
        db.commit()
        return deleteInvListMember
