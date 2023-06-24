from database.connection import db
from datetime import datetime

class Wibe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood_input = db.Column(db.String(300), nullable=False)
    pinecone_vector_id = db.Column(db.String, nullable=False)
    country = db.Column(db.String(120))  # Add this line for the country
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a relationship to the User model
    user = db.relationship('User', backref=db.backref('wibes', lazy=True))

    def __repr__(self):
        return f'<Wibe {self.mood_input}>'
