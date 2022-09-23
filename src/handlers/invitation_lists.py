from flask import Blueprint, render_template, request
from models.event import Event
# from models.post import Post
from models.settings import db
from utils.app_name import app_name
from utils.user_helper import getCurrentUser, isLoggedIn, redirectToLogin, redirectToRoute
#  from utils.mail import sendEmail

event_handlers = Blueprint("event_handlers", __name__)

# list all events 
@event_handlers.route('/events_list', methods=["GET", "POST"])
def events_list():
    if request.method == "GET":
        if isLoggedIn():
            return render_template("events_list.html",
                                    app_name=app_name,
                                    user=getCurrentUser(),
                                    events=db.query(Event)
                                    .filter_by(deleted_at=None)
                                    .filter_by(event_host_id=getCurrentUser().id)
                                    .order_by(Event.created_at).all())
        else:
            return redirectToLogin()

    elif request.method == "GET":
        return render_template("404.html", app_name=app_name,
                               user=getCurrentUser())

# create read update delete
@event_handlers.route('/event', methods=["GET", "POST"])
def event():
    event_id = request.args.get('event_id')
    user = getCurrentUser()
    action = request.args.get('action')
    readEvent = db.query(Event).filter_by(id=event_id).filter_by(event_host_id=user.id).first()
    if request.method == "POST":
        if event_id is None and action == "create":
            event_host_id = user.id
            event_name = request.form.get('event_name')
            event_start_date = request.form.get('event_start_date')
            event_end_date = request.form.get('event_end_date')
            event_time_start = request.form.get('event_time_start')
            event_duration_minutes = request.form.get('event_duration_minutes')
            event_recurrence_period = request.form.get('event_recurrence_period')
            send_event_invite_before_days = request.form.get('send_event_invite_before_days')
            send_event_invite_at_hour = request.form.get('send_event_invite_at_hour')
            event_remind_before_hours = request.form.get('event_remind_before_hours')
            invitation_list_id = request.form.get('invitation_list_id')

            Event.create(event_host_id=event_host_id, 
                        event_name=event_name, 
                        event_start_date=event_start_date, 
                        event_end_date=event_end_date, 
                        event_time_start=event_time_start, 
                        event_duration_minutes=event_duration_minutes, 
                        event_recurrence_period=event_recurrence_period, 
                        send_event_invite_before_days=send_event_invite_before_days, 
                        send_event_invite_at_hour=send_event_invite_at_hour, 
                        event_remind_before_hours=event_remind_before_hours, 
                        invitation_list_id=invitation_list_id)

            return redirectToRoute("event_handlers.events_list") \
                if isLoggedIn() else redirectToLogin()

        elif readEvent is not None and action == "update":
            if readEvent.event_host_id == getCurrentUser().id:
                event_id=event_id
                event_host_id = user.id
                event_name = request.form.get('event_name')
                event_start_date = request.form.get('event_start_date')
                event_end_date = request.form.get('event_end_date')
                event_time_start = request.form.get('event_time_start')
                event_duration_minutes = request.form.get('event_duration_minutes')
                event_recurrence_period = request.form.get('event_recurrence_period')
                send_event_invite_before_days = request.form.get('send_event_invite_before_days')
                send_event_invite_at_hour = request.form.get('send_event_invite_at_hour')
                event_remind_before_hours = request.form.get('event_remind_before_hours')
                invitation_list_id = request.form.get('invitation_list_id')
                
                Event.update(
                            id=event_id,
                            event_host_id=event_host_id,
                            event_name=event_name, 
                            event_start_date=event_start_date, 
                            event_end_date=event_end_date, 
                            event_time_start=event_time_start, 
                            event_duration_minutes=event_duration_minutes, 
                            event_recurrence_period=event_recurrence_period, 
                            send_event_invite_before_days=send_event_invite_before_days, 
                            send_event_invite_at_hour=send_event_invite_at_hour, 
                            event_remind_before_hours=event_remind_before_hours, 
                            invitation_list_id=invitation_list_id)
                notification_msg = "You have changed Event successfully!"
                print(notification_msg)

                return redirectToRoute("event_handlers.events_list") \
                    if isLoggedIn() else redirectToLogin()
            else:
                notification_msg = "You don't have permissions to change Event!"
                print(notification_msg)

                return redirectToRoute("event_handlers.events_list") \
                    if isLoggedIn() else redirectToLogin()

        elif readEvent is not None and action == "delete":
            if readEvent.event_host_id == user.id:
                Event.delete(id=event_id)
                notification_msg = "You have deleted Event successfully!"
                print(notification_msg)
            else:
                notification_msg = "You don't have permissions to delete Event!"
                print(notification_msg)
            return redirectToRoute("event_handlers.events_list") \
                if isLoggedIn() else redirectToLogin()
        else:
            return render_template("404.html", app_name=app_name,
                                  user=getCurrentUser())

    if request.method == "GET":
        if readEvent is None and action == "create":  # redirect to 404
            return render_template("event_form.html", 
                                  app_name=app_name,
                                  user=user,
                                  event_host_id=user.id,
                                  action=action) \
                if isLoggedIn() else redirectToLogin()

        elif readEvent is not None and action == "update":
            return render_template("event_form.html", app_name=app_name,
                                   action=action,
                                   user=getCurrentUser(),
                                   event_id=readEvent.id,
                                   event_host_id=user.id,
                                   event_name=readEvent.event_name, 
                                   event_start_date=readEvent.event_start_date, 
                                   event_end_date=readEvent.event_end_date, 
                                   event_time_start=readEvent.event_time_start,  
                                   event_duration_minutes=readEvent.event_duration_minutes, 
                                   event_recurrence_period=readEvent.event_recurrence_period, 
                                   send_event_invite_before_days=readEvent.send_event_invite_before_days, 
                                   send_event_invite_at_hour=readEvent.send_event_invite_at_hour, 
                                   event_remind_before_hours=readEvent.event_remind_before_hours, 
                                   invitation_list_id=readEvent.invitation_list_id) \
                if isLoggedIn() else redirectToLogin()

        elif readEvent is None:  # redirect to 404
            return render_template("404.html", app_name=app_name,
                                  user=getCurrentUser())