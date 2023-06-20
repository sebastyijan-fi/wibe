# routes/submit_wibe.py
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
# import necessary functions and models to process and store the wibe

bp = Blueprint('submit_wibe', __name__, url_prefix='/submit-wibe')

@bp.route('', methods=['POST'])
@login_required  # Makes sure the user is logged in before they can submit a wibe
def submit_wibe_route():
    wibeData = request.get_json()  # Get the submitted wibe data
    text = wibeData.get('text')
    country = wibeData.get('country')

    # Process the wibe text and store it in your databases (Postgres and Pinecone)
    # You would write your own function to do this

    return jsonify({"status": "success"})  # Return a success status
