# routes/login.py
from flask import Blueprint, request, jsonify, session
from flask_login import login_user
from auth.login import login

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('', methods=['POST'])  # Changed from '/' to ''
def login_route():
    data = request.get_json()
    user = login(data['username'], data['password'])
    if not user:
        return jsonify({'error': 'Invalid username or password'}), 401

    # You have authenticated the user, now store the user id in session
    session['user_id'] = user.id

    login_user(user)
    return jsonify({'message': 'Logged in successfully'})
