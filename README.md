# Spotify Review Analysis Chatbot

This project provides a chatbot interface for analyzing Spotify reviews. The chatbot uses embeddings generated from review texts to find similar reviews and generate summaries based on user queries.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `streamlit`
  - `sentence-transformers`
  - `numpy`
  - `scikit-learn`
  - `motor`
  - `openai`
- A running instance of MongoDB with the necessary data

## Setup

1. **Install Required Packages**: Ensure all required Python packages are installed. You can do this using pip:

   ```bash
   pip install streamlit sentence-transformers numpy scikit-learn motor openai
   ```

2. **Environment Variables**: Create a `.env` file in the `app` directory with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   MONGO_DB_URL=your_mongo_db_url
   MONGO_DB_NAME=your_mongo_db_name
   MONGO_DB_COLLECTION=your_mongo_db_collection
   ```

3. **MongoDB Data**: Ensure your MongoDB instance is running and contains the necessary data. The data should include review texts and their corresponding embeddings.

## Running the Application

1. **Navigate to the Application Directory**: Open a terminal and navigate to the directory containing `main.py`.

2. **Run the Streamlit Application**: Use the following command to start the Streamlit application:

   ```bash
   streamlit run app/main.py
   ```

3. **Interact with the Chatbot**: Open the provided URL in your browser (usually `http://localhost:8501`). You can now interact with the chatbot by entering queries about Spotify reviews.

## Code Overview

### Main Components

- **main.py**: The main entry point for the Streamlit application. It handles user input, fetches data from MongoDB, calculates similarities, and generates summaries.
  ```python:app/main.py
  startLine: 1
  endLine: 40
  ```

- **db.py**: Contains functions for interacting with the MongoDB database asynchronously.
  ```python:app/db.py
  startLine: 1
  endLine: 14
  ```

- **chatbot.py**: Defines the `Chatbot` class, which uses the OpenAI API to generate summaries based on user queries and review texts.
  ```python:app/chatbot.py
  startLine: 1
  endLine: 31
  ```

- **constant.py**: Stores constants and environment variable configurations.
  ```python:app/constant.py
  startLine: 1
  endLine: 21
  ```

## Notes

- Ensure your MongoDB instance is running and accessible before starting the application.
- The chatbot uses the OpenAI API for generating summaries. Make sure you have a valid API key and sufficient quota.