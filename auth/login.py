# auth/login.py

from werkzeug.security import check_password_hash
from models.user import User

def login(username, password):
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return None

    return user
