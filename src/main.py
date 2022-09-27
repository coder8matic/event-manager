from flask import Flask
# load environmental variables from .env file
from dotenv import load_dotenv
# Environment variables need to be imported before modules import
load_dotenv()

from handlers.auth import authentication_handlers  # noqa E402
from handlers.event import event_handlers  # noqa E402
from handlers.invitation_list import invitation_list_handlers  # noqa E402
from handlers.invitation_list_member import inv_list_member_handlers  # noqa E402
from models.settings import db  # noqa E402
from models.user import User  # noqa E402
from models.event import Event  # noqa E402
from models.event_item import EventItem  # noqa E402
from models.event_item_user import EventItemUser  # noqa E402
from models.invitation_list import InvitationList  # noqa E402
from models.invitation_list_member import InvitationListMember  # noqa E402
from utils.user_helper import isLoggedIn, redirectToRoute, getCurrentUser  # noqa E402
# from utils.app_name import app_name  # noqa E402


# Check if everything is OK with DB. If DB do not exist create DB
try:
    db.query(User).first()
    print("Table 'User' is OK")
    db.query(Event).first()
    print("Table 'Event' is OK")
    db.query(EventItem).first()
    print("Table 'EventItem' is OK")
    db.query(EventItemUser).first()
    print("Table 'EventItemUser' is OK")
    db.query(InvitationList).first()
    print("Table 'InvitationList' is OK")
    db.query(InvitationListMember).first()
    print("Table 'InvitationListMember' is OK")

except:   # noqa E722
    try:
        db.create_all()
        print("DB created")
    except:   # noqa E722
        print("Something went wrong with DB check procedure")
# end of DB check

app = Flask(__name__)
app.register_blueprint(authentication_handlers)
app.register_blueprint(event_handlers)
app.register_blueprint(invitation_list_handlers)
app.register_blueprint(inv_list_member_handlers)

print('up and running')


@app.route('/', methods=["GET"])
def index():
    return redirectToRoute("event_handlers.events_list") \
        if isLoggedIn() else redirectToRoute("auth.login")


if __name__ == '__main__':
    app.run(use_reloader=True)
