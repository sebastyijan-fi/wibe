# database/connection.py

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

db = SQLAlchemy()

def init_db(app):
    print("Initializing the database...")
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    print("Database initialized.")
