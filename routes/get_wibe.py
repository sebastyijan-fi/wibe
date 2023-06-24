from flask import Blueprint, request, jsonify
from flask_login import login_required
from models.wibe import Wibe
from database.connection import db
import os
import pinecone
from flask_login import current_user

bp = Blueprint('get_wibe', __name__, url_prefix='/get-wibe')

pinecone.init(api_key=os.getenv("PKEY"), environment='us-east1-gcp')
index = pinecone.Index("wibe-moods")

@bp.route('', methods=['GET'])
@login_required
def get_latest_wibe_route():
    # Fetch the latest Wibe added to the database
    latest_wibe = db.session.query(Wibe).order_by(Wibe.id.desc()).first()

    if not latest_wibe:
        return jsonify({"error": "No wibes found."}), 404

    # Fetch the vector of the latest Wibe from Pinecone
    vector = index.fetch(ids=[latest_wibe.pinecone_vector_id])

    if not vector or not vector.get('vectors', {}).get(latest_wibe.pinecone_vector_id, None):
        return jsonify({"error": f"Vector not found for Wibe with ID: {latest_wibe.id} with {vector}."}), 404

    latest_wibe_vector = list(vector.get('vectors').values())[0]['values']

    # Query Pinecone for the top 10 most similar vectors
    similar_vectors = index.query(queries=[latest_wibe_vector], top_k=10)

    if not similar_vectors or not similar_vectors.get('results'):
        return jsonify({"error": "No similar wibes found."}), 404

    # Extract the 'matches' from the response
    matches = similar_vectors.get('results')[0]['matches']

    # Set a minimum similarity score
    min_similarity_score = 0.1

    # Filter out matches with a similarity score below the minimum
    filtered_matches = [match for match in matches if match['score'] >= min_similarity_score]

    # Extract the IDs of the filtered matches
    filtered_match_ids = [match['id'] for match in filtered_matches]

    # Fetch the wibes corresponding to the filtered matches from the database
    similar_wibes = db.session.query(Wibe).filter(Wibe.pinecone_vector_id.in_(filtered_match_ids)).filter(Wibe.user_id != current_user.id).all()

    # Format the Wibes for the response
    response_wibes = [
        {
            "id": wibe.id,
            "mood_input": wibe.mood_input,
            "user_id": wibe.user_id,
            "country": wibe.country,
            "timestamp": wibe.timestamp.isoformat() + "Z"
        } for wibe in similar_wibes
    ]

    # Get the latest wibe of the current user and append it to the response
    user_latest_wibe = db.session.query(Wibe).filter_by(user_id=current_user.id).order_by(Wibe.id.desc()).first()

    if user_latest_wibe:
        response_wibes.append({
            "id": user_latest_wibe.id,
            "mood_input": user_latest_wibe.mood_input,
            "user_id": user_latest_wibe.user_id,
            "country": user_latest_wibe.country,
            "timestamp": user_latest_wibe.timestamp.isoformat() + "Z"
        })

    return jsonify(response_wibes)


