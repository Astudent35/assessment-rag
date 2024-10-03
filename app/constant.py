import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_DB_COLLECTION = os.getenv("MONGO_DB_COLLECTION")

SUMMARIZATION_PROMPT = """
###User Query###
User Query: {query} 
The question was asked at {timestamp}

###List of Reviews###
List of Reviews: {reviews}

###Objective###
Your objective is to generate a summary given the user query and list of reviews.
"""