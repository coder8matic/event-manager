from models.settings import db
from models.user import User
from models.event import Event
from models.event_member import EventMember
from models.event_member_user import EventMemberUser
from models.invitation_list import InvitationList
from models.invitation_list_member import InvitationListMember

db.create_all()
