from sentence_transformers import SentenceTransformer
from concurrent.futures import ThreadPoolExecutor, as_completed
from pymongo import MongoClient
import numpy as np
import pandas as pd

from app.constant import MONGO_DB_URL

df = pd.read_csv('/Users/masa/Desktop/assessment-rag/CLEANED_SPOTIFY_REVIEWS_v2.csv')

 
# MongoDB connection
client = MongoClient(MONGO_DB_URL)
db = client['spotify_reviews_db']
collection = db['reviews_with_embeddings']


model = SentenceTransformer('all-MiniLM-L6-v2')

batch_size = 256  # Increase this if your system can handle it

# Insert data into MongoDB with batch processing
for i in range(0, len(df), batch_size):
    batch_reviews = df['review_text_with_metadata'].tolist()[i:i+batch_size]
    batch_embeddings = model.encode(batch_reviews, batch_size=batch_size)

    # Prepare MongoDB documents
    documents = []
    for j, review in enumerate(batch_reviews):
        document = {
            'review_text': review,
            'embedding': batch_embeddings[j].tolist()  # Store as list for MongoDB
        }
        documents.append(document)
    
    # Insert batch into MongoDB
    collection.insert_many(documents)

print("Embeddings successfully generated and inserted into MongoDB.")