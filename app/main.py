import asyncio
import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from chatbot import Chatbot
from db import fetch_data

model = SentenceTransformer('all-MiniLM-L6-v2')
st.title("Spotify Review Analysis Chatbot")
chatbot = Chatbot()

user_query = st.text_input("Ask a question about Spotify reviews:")


if st.button('Submit'):
    query_embedding = model.encode([user_query])

    data = asyncio.run(fetch_data())

    # Separate embeddings and review texts
    all_embeddings, review_texts = zip(*data)

    # Convert to numpy arrays
    all_embeddings = np.array(all_embeddings)
    query_embedding = np.array(query_embedding)

    # Calculate cosine similarities
    similarities = cosine_similarity(query_embedding, all_embeddings)

    # Get top n similar reviews
    top_n = np.argsort(similarities[0])[-5:][::-1]
    reviews = [review_texts[idx] for idx in top_n]
    for idx in top_n:
        st.write(f"Review: {review_texts[idx]}, Similarity: {similarities[0][idx]}")
    
     # Debugging: Check if reviews are being passed correctly
    st.write(f"Reviews for summarization: {reviews}")
    summary = chatbot.generate_summerization(user_query, reviews)    
    st.write(f"Generated Summary: {summary}")