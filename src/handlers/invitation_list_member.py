from flask import Blueprint, render_template, request
from models.invitation_list import InvitationList
from models.invitation_list_member import InvitationListMember
from models.settings import db
from utils.app_name import app_name
from utils.user_helper import (getCurrentUser, isLoggedIn,
                               redirectToLogin, redirectToRoute)

inv_list_member_handlers = Blueprint("inv_list_member_handlers", __name__)


# list all
@inv_list_member_handlers.route('/invitation_list_members',
                                methods=["GET", "POST"])
def invitation_list_members():
    inv_list_id = request.args.get('inv_list_id')
    if request.method == "GET":
        if isLoggedIn():
            return render_template("invitation_list_members.html",
                                   app_name=app_name,
                                   user=getCurrentUser(),
                                   InvList=db.query(InvitationList)
                                   .filter_by(deleted_at=None)
                                   .filter_by(id=inv_list_id)
                                   .filter_by(list_owner_id=getCurrentUser()
                                              .id).first(),

                                   InvListMembers=db.query(InvitationListMember) # noqa E501
                                   .filter_by(deleted_at=None)
                                   .filter_by(list_id=inv_list_id).all())
# TODO - implement alphabet order
                              #    .order_by(InvitationListMember)
                                #  .list_member.email).all())
        else:
            return redirectToLogin()

    elif request.method == "GET":
        print('404-1')
        return render_template("404.html", app_name=app_name,
                               user=getCurrentUser())


# create read (update) delete
@inv_list_member_handlers.route('/invitation_list_member',
                                methods=["GET", "POST"])
def invitation_list_member():
    inv_list_id = request.args.get('inv_list_id')
    print('inv_list_id:')
    print(inv_list_id)
    action = request.args.get('action')
    inv_list_member_email = request.form.get('new_inv_list_member_email')
    print('inv_list_member_email:')
    print(inv_list_member_email)
    inv_list_member_id = request.args.get('inv_list_member_id')

    if request.method == "POST":
        if inv_list_id is not None and inv_list_member_email is not None \
                and action == "create":  # POST method CREATE
            if InvitationListMember.list.list_owner_id == getCurrentUser().id:

                InvitationListMember.create(list_id=inv_list_id,
                                            list_member_email=inv_list_member_email, # noqa E501
                                            )

                return redirectToRoute("invitation_list_handlers.invitation_list_members") \
                    if isLoggedIn() else redirectToLogin()  # noqa E501

            else:
                notification_msg = "You don't have permissions \
                                    to add Member on this Invitation List!"
                print(notification_msg)

        elif inv_list_member_id is not None and action == "delete":   # POST method DELETE # noqa E501
            if InvitationListMember.list_id.list_owner_id == getCurrentUser():
                InvitationListMember.delete(id=inv_list_member_id)
                notification_msg = "You have successfully deleted Member \
                                    from this Invitation List!"
                print(notification_msg)
            else:
                notification_msg = "You don't have permissions to \
                                    delete Member from this Invitation List!"
                print(notification_msg)
            return redirectToRoute("invitation_list_handlers.invitation_lists") \
                if isLoggedIn() else redirectToLogin()  # noqa E501
        else:
            print('404-2')
            return render_template("404.html", app_name=app_name,
                                   user=getCurrentUser())

    if request.method == "GET":
        print('404-3')
        return render_template("404.html", app_name=app_name,
                               user=getCurrentUser())
