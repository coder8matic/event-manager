from flask import Flask  # , render_template
# load environmental variables from .env file
from dotenv import load_dotenv
# Environment variables need to be imported before modules import
load_dotenv()


from handlers.auth import authentication_handlers  # noqa E402
from handlers.dashboard import dashboard_handlers  # noqa E402
from models.settings import db  # noqa E402
from models.user import User  # noqa E402
# from models.event import Event
# from models.event_item import EventItem
# from models.event_item_user import EventItemUser
# from models.invitation_list import InvitationList
# from models.invitation_list_item import InvitationListItem
from utils.user_helper import isLoggedIn, redirectToRoute, getCurrentUser  # noqa E402
# from utils.app_name import app_name  # noqa E402

# Check if everything is OK with DB. If DB do not exist create DB
try:
    db.query(User).first()
    print("Table 'User' is OK")

except:   # noqa E722
    try:
        db.create_all()
        print("DB created")
    except:   # noqa E722
        print("Something went wrong with DB check procedure")
# end of DB check

app = Flask(__name__)
app.register_blueprint(authentication_handlers)
app.register_blueprint(dashboard_handlers)
print('up and running')


@app.route('/', methods=["GET"])
def index():
    return redirectToRoute("dashboard.dashboard") \
        if isLoggedIn() else redirectToRoute("auth.login")


if __name__ == '__main__':
    app.run(use_reloader=True)  # , debug=True)
