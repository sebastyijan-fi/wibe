from app import app
from database.connection import db
from models.user import User
from models.wibe import Wibe

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_db()
