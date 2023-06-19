from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from database.connection import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    country = db.Column(db.String(120), index=True)
    avatar = db.Column(db.String(500))  # The avatar is stored as a URL
    registration_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_active_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    notification_settings = db.Column(db.JSON)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
