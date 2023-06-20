import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OKEY")


# Define a sample text
text = "I am feeling great today!"

# Request mood scores from OpenAI
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that outputs mood scores for text in JSON format. The moods you should consider are: Happiness, Contentment, Pleasure, Excitement, Hope, Optimism, Safety, Comfort, Reliability, Astonishment, Amazement, Wonder, Sorrow, Disappointment, Unhappiness, Anxiety, Worry, Unease, Reflective Sadness, Contemplative Longing, Calm, Peace, Tranquility, Curiosity, Fascination, Engagement, Affection, Warmth, and Fondness.",
        },
        {
            "role": "user",
            "content": f"Can you give me the mood scores for the text and only reply in JSON format!!! '{text}'?",
        },
    ],
)

print(response.choices[0].message["content"])
