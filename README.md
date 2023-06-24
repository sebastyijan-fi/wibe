# Wibe

Wibe is a global mood sharing platform. It's not about your status, who you're with, or where you are. It's about your current mood, plain and simple.

## Project Overview

Wibe was inspired by the belief that every individual's emotional state matters and should be acknowledged. The aim was to create a platform where people around the world could express their current mood anonymously, fostering a sense of unity and connection.

The application is built on the foundations of Flask, a popular web framework in Python, and uses Pinecone, a vector database for nearest neighbor search, to maintain the chronological order of the mood posts. PostgreSQL was used as the main database to store user mood data. The front-end was built using HTML, CSS, and JavaScript, with a special focus on a minimal, easy-to-use, and intuitive interface.

Wibe uses OpenAI's GPT-3 model to create mood dimensions and convey the moods in a more expressive and human-like manner. It also leverages an IP location API to provide a geographical context to each shared mood.

## Future Plans

Looking forward, there are plans to enhance Wibe with a graphical dashboard to visualize mood evolution. This will allow users to track their own mood history and reflect upon their emotional journey. Furthermore, generative Text2Img features might be introduced, enabling users to express their moods visually if they wish to do so.

Stay tuned for more exciting features and improvements on Wibe!
