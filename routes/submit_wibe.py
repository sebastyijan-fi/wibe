from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.wibe import Wibe
from database.connection import db

# Import your new function
from .pinecone_process import process_text_and_store


bp = Blueprint('submit_wibe', __name__, url_prefix='/submit-wibe')

@bp.route('', methods=['POST'])
@login_required
def submit_wibe_route():
    wibeData = request.get_json()
    text = wibeData.get('text')
    country = wibeData.get('country')

    # Call your new function and get the vector ID and mood scores
    vector_id, mood_scores = process_text_and_store(text)

    new_wibe = Wibe(user_id=current_user.id, mood_input=text, pinecone_vector_id=vector_id, country=country)

    db.session.add(new_wibe)
    db.session.commit()

    return jsonify({"status": "success"})
