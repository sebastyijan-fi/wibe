# routes/logout.py
from flask import Blueprint, session, jsonify
from flask_login import logout_user

bp = Blueprint('logout', __name__, url_prefix='/logout')

@bp.route('', methods=['POST'])  # Changed from '/' to ''
def logout_route():
    user_id = session.get('user_id')
    if user_id is None:
        return jsonify({'error': 'No active session'}), 401

    # Delete the user id from the session
    del session['user_id']

    # Use Flask-Login's logout_user function
    logout_user()

    return jsonify({'status': 'success'})

