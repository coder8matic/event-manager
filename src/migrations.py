from src.models.settings import db
from src.models.user import User
from src.models.event import Event
from src.models.event_item import EventItem
from src.models.event_item_user import EventItemUser
from src.models.invitation_list import InvitationList
from src.models.invitation_list_item import InvitationListItem

db.create_all()