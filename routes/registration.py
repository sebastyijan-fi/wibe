# routes/register.py

from flask import Blueprint, request, jsonify, session  # Import session
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from models.user import User
from database.connection import db

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('', methods=['POST'])  # Changed from '/' to ''
def register():
    data = request.get_json()  # Get data from POST request
    if not data:
        raise BadRequest("No input data provided")

    # Basic validation: check that username, email, and password are provided
    for field in ['username', 'email', 'password']:
        if not data.get(field):
            raise BadRequest(f"'{field}' is required.")

    # More validation could be added here (e.g. check email format, password complexity)

    # Create a new user
    user = User()
    user.username = data['username']
    user.email = data['email']
    user.set_password(data['password'])

    # Additional user fields can be set here based on input data

    try:
        # Add the new user to the database
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        # The username or email already exists
        db.session.rollback()
        raise BadRequest("Username or email already in use")

    # Set the session variable for the user
    session['user_id'] = user.id

    # Return a success message and the new user's id
    return jsonify(message='User registered successfully', id=user.id), 201
