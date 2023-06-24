import os
import pinecone
from dotenv import load_dotenv
from models.wibe import Wibe
from database.connection import db
from app import create_app  # Importing create_app from app.py

load_dotenv()

pinecone_api_key = os.getenv("PKEY")
pinecone.init(api_key=pinecone_api_key, environment='us-east1-gcp')

index_name = "wibe-moods"
index = pinecone.Index(index_name)
index_stats = index.describe_index_stats()
print(index_stats)

app = create_app()  # Create a Flask app instance

with app.app_context():
    wibes = db.session.query(Wibe).all()

    for wibe in wibes:
        print(f"Wibe ID: {wibe.id}, Mood Input: {wibe.mood_input}, User ID: {wibe.user_id}, Country: {wibe.country}")
        print(f"Trying to retrieve Vector ID: {wibe.pinecone_vector_id}")
        vector = index.fetch(ids=[wibe.pinecone_vector_id])
        print(f"Fetch response: {vector}")
        if vector.id_errors:
            print(f"Error in retrieving Vector ID: {wibe.pinecone_vector_id}. Error: {vector.id_errors}")
        elif vector.result is not None and vector.result.get('vectors', None):
            print(f"Vector ID: {wibe.pinecone_vector_id}, Vector: {vector.result['vectors']}")
        else:
            print(f"Vector ID: {wibe.pinecone_vector_id}, Vector not found in Pinecone index.")

