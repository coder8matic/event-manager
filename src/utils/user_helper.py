import json
from flask import make_response, redirect, request, url_for
# from models.settings import db
from models.user import User
from utils.redis_settings import r


def isLoggedIn():
    session_token = request.cookies.get("session_token")
    logged_user = getCurrentUser() if session_token else None

    return logged_user is not None  # Returns True or False


def redirectToLogin():
    return redirectToRoute("auth.login")


def getCurrentUser():
    session_token = request.cookies.get("session_token")
    user_redis = r.get(session_token)
    if user_redis is None:
        User is None
    else:
        user_json = json.loads(user_redis)
        User.id = int(user_json.get('id'))
        User.email = user_json.get('email')
        User.password = user_json.get('password')

    return User


def redirectToRoute(route, **kwargs):
    return make_response(redirect(url_for(route), **kwargs))
