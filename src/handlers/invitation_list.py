from flask import Blueprint, render_template, request
from models.invitation_list import InvitationList
from models.settings import db
from utils.app_name import app_name
from utils.user_helper import (getCurrentUser, isLoggedIn,
                               redirectToLogin, redirectToRoute)

invitation_list_handlers = Blueprint("invitation_list_handlers", __name__)


# list all
@invitation_list_handlers.route('/invitation_lists', methods=["GET", "POST"])
def invitation_lists():
    if request.method == "GET":
        if isLoggedIn():
            return render_template("invitation_lists.html",
                                   app_name=app_name,
                                   user=getCurrentUser(),
                                   inv_lists=db.query(InvitationList)
                                   .filter_by(deleted_at=None)
                                   .filter_by(list_owner_id=getCurrentUser().id)  # noqa E501
                                   .order_by(InvitationList.list_name).all())
        else:
            return redirectToLogin()

    elif request.method == "GET":
        return render_template("404.html", app_name=app_name,
                               user=getCurrentUser())


# create read update delete
@invitation_list_handlers.route('/invitation_list', methods=["GET", "POST"])
def invitation_list():
    inv_list_id = request.args.get('inv_list_id')
    user = getCurrentUser()
    action = request.args.get('action')
    readInvList = db.query(InvitationList) \
                    .filter_by(id=inv_list_id) \
                    .filter_by(list_owner_id=user.id).first()
    if request.method == "POST":
        if inv_list_id is None and action == "create":  # POST method
            list_name = request.form.get('list_name')
            list_owner_id = user.id

            InvitationList.create(list_name=list_name,
                                  list_owner_id=list_owner_id,
                                  )

            return redirectToRoute("invitation_list_handlers.invitation_lists") \
                if isLoggedIn() else redirectToLogin()

        elif readInvList is not None and action == "update":  # POST method
            if readInvList.list_owner_id == getCurrentUser().id:
                inv_list_id = inv_list_id
                inv_list_name = request.form.get('list_name')
                inv_list_owner_id = getCurrentUser().id

                InvitationList.update(
                                     id=inv_list_id,
                                     list_name=inv_list_name,
                                     list_owner_id=inv_list_owner_id,
                                     )
                notification_msg = "You have updated Invitation List successfully!"  # noqa E501
                print(notification_msg)

                return redirectToRoute("invitation_list_handlers.invitation_lists") \
                    if isLoggedIn() else redirectToLogin()
            else:
                notification_msg = "You don't have permissions to change Invitation List!"  # noqa E501
                print(notification_msg)

                return redirectToRoute("invitation_list_handlers \
                                        .invitation_lists") \
                    if isLoggedIn() else redirectToLogin()

        elif readInvList is not None and action == "delete":   # POST method
            if readInvList.list_owner_id == user.id:
                InvitationList.delete(id=inv_list_id)
                notification_msg = "You have deleted Invitation List successfully!"  # noqa E501
                print(notification_msg)
            else:
                notification_msg = "You don't have permissions \
                                    to delete Invitation List!"
                print(notification_msg)
            return redirectToRoute("invitation_list_handlers.invitation_lists") \
                if isLoggedIn() else redirectToLogin()
        else:
            return render_template("404.html", app_name=app_name,
                                   user=getCurrentUser())

    if request.method == "GET":
        if readInvList is None and action == "create":  # GET method
            return render_template("invitation_list_form.html",
                                   app_name=app_name,
                                   user=user,
                                   event_host_id=user.id,
                                   action=action,
                                   inv_list=readInvList) \
                if isLoggedIn() else redirectToLogin()

        elif readInvList is not None and action == "update":
            return render_template("invitation_list_form.html",
                                   app_name=app_name,
                                   action=action,
                                   user=getCurrentUser(),
                                   inv_list=readInvList) \
                if isLoggedIn() else redirectToLogin()

        elif readInvList is None:  # redirect to 404
            return render_template("404.html", app_name=app_name,
                                   user=getCurrentUser())
