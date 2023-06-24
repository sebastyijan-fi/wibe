import os
import json
import openai
import pinecone
import numpy as np
from dotenv import load_dotenv
import uuid

load_dotenv()

openai.api_key = os.getenv("OKEY")
pinecone_api_key = os.getenv("PKEY")

if pinecone_api_key is None:
    raise ValueError("Pinecone API key not found in environment variables.")

pinecone.init(api_key=pinecone_api_key, environment='us-east1-gcp')

# Define your Pinecone index
index_name = "wibe-moods"

# Check if the index exists, if not, create it
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, metric='cosine', dimension=28, shards=1)

# Initialize the index
index = pinecone.Index(index_name)

# Define a sample text
text = "Went for a walk with the dog. It was a beautiful day. I felt happy. Have to go to work tomorrow though :("

# Request mood scores from OpenAI
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that outputs mood scores for text in JSON format. The moods you should consider are: Happiness, Contentment, Pleasure, Excitement, Hope, Optimism, Comfort, Reliability, Astonishment, Amazement, Wonder, Sorrow, Disappointment, Unhappiness, Anxiety, Worry, Unease, Reflective Sadness, Contemplative Longing, Calm, Peace, Tranquility, Curiosity, Fascination, Engagement, Affection, Warmth, and Fondness.",
        },
        {
            "role": "user",
            "content": f"reply only in JSON format, with only the moods as key values. Values range from 0-1!!! Exctract from here: '{text}'?",
        },
    ],
)

# Directly get the mood scores string from the response
mood_scores_str = response.choices[0].message["content"] # type: ignore

# Convert the mood scores string to a Python dictionary
mood_scores_dict = json.loads(mood_scores_str)

# Print mood_scores_dict to verify its content
print(mood_scores_dict)

# Convert the dictionary values (mood scores) to a list of floats
mood_scores_list = [float(score) for score in mood_scores_dict.values()]

# Generate a unique vector id
vector_id = str(uuid.uuid4())

# Save mood vector to Pinecone
index.upsert([(vector_id, mood_scores_list)])


print(f"Inserted mood vector to Pinecone with id {vector_id}")

