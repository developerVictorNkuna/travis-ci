import sys

sys.path.append("C:\\python-testing\\flask-app\\3.1 starter_code\\starter_code\\testing-python-apps\\section8\\video_code\\security.py")
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
