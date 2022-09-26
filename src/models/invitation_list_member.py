import hashlib
from models.settings import db
from models.user import User
from utils.string_helper import random_string
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
               list_member_email,
               ):

        # Find member in User Table if exists and extract id
        MemberExists = db.query(User) \
                    .filter_by(User.email == list_member_email) \
                    .first()
        if MemberExists is not None:
            list_member_id = MemberExists.id
        # Create User if member does not exists in User Table
        elif MemberExists is None:
            user_email = list_member_email
            user_password = random_string(30)
            list_member_id = User.create(email=user_email,
                                         password=hashlib
                                         .sha256(user_password.encode())
                                         .hexdigest()).id
            print('my new: list_member_id')
            print(list_member_id)

        # check if member is already on list
        find_member_in_inv_list = db.query(InvitationListMember) \
            .filter_by(list_id=list_id) \
            .filter_by(list_member_id).first()

        if find_member_in_inv_list is None:
            newInvListMember = self(list_id=list_id,
                                    list_member_id=list_member_id,
                                    )

        elif find_member_in_inv_list is not None \
                and find_member_in_inv_list.deleted_at is not None:
            newInvListMember = find_member_in_inv_list(deleted_at=None,
                                                       updated_at=datetime
                                                       .utcnow())
            notification_msg = "Member added on list (Undeleted)"
            print(notification_msg)

        else:  # find_member_in_inv_list is not None:
            notification_msg = "Member is already on list"
            print(notification_msg)
            return notification_msg

        db.add(newInvListMember)
        db.commit()
        return newInvListMember

    # TODO: Not needed because we only add and delete members

    # @classmethod
    # def update(self,
    #            id,
    #            list_member_email,
    #            ):

    #     updateInvListMember = db.query(InvitationListMember) \
    #                         .filter_by(id=id).first()
    #     updateInvListMember.list_member_id = list_member_id
    #     updateInvListMember.updated_at = datetime.utcnow()

    #     db.add(updateInvListMember)
    #     db.commit()
    #     return updateInvListMember

    @classmethod
    def delete(self, id):
        deleteInvListMember = db.query(InvitationListMember) \
                            .filter_by(id=id) \
                            .filter_by(deleted_at=None).first()
        deleteInvListMember.deleted_at = datetime.utcnow()

        db.add(deleteInvListMember)
        db.commit()
        return deleteInvListMember
