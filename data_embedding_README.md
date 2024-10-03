# Note
- In order to generate embeddings, the resources that I was using are limited.
- The dataset is containing about 3.4 million rows and I am not able to generate embeddings for all of them.
- I have generated embeddings for about 100,000 rows and stored them in MongoDB.
- Also to generate embeddings, this part usually requires a lot of RnD but I used models which were able to run locally which much memory usage.
- The quality of the the generated response would be good if all the data is used but I was not able to generate embeddings for all the data.
- In order to optimize the program it self, I would have to use a different model But that would require a lot of RnD.

## Data preprocessing Overview 

1. **Import Data**: The notebook reads the raw Spotify reviews from a CSV file using `pandas`.

2. **Data Cleaning**:
   - Drops unnecessary columns, such as the index column `Unnamed: 0`.
   - Converts all review text to lowercase and removes leading/trailing spaces.
   - Removes rows with missing or null values in critical columns like `review_text` and `review_rating`.

3. **Add Metadata**: Creates a new column `review_text_with_metadata` that combines review text with additional metadata such as user rating, likes, app version, and timestamp.
  - This is done to make the data more useful for RAG.

## Generate Embedding Script

This script is designed to generate embeddings for Spotify reviews and store them in a MongoDB database. It utilizes the `sentence-transformers` library to convert text data into numerical embeddings, which can be used for various machine learning tasks such as clustering, classification, or similarity search.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `sentence-transformers`
  - `pandas`
  - `numpy`
  - `pymongo`
- A running instance of MongoDB

## Setup

1. **Install Required Packages**: Ensure all required Python packages are installed. You can do this using pip:

   ```bash
   pip install sentence-transformers pandas numpy pymongo
   ```

2. **MongoDB Connection**: Update the `MONGO_DB_URL` in the `app.constant` module to point to your MongoDB instance.

3. **CSV File**: Ensure the CSV file `CLEANED_SPOTIFY_REVIEWS_v2.csv` is located at `/Users/masa/Desktop/assessment-rag/`.

## Process Overview

1. **Load Data**: The script reads Spotify reviews from a CSV file using `pandas`.

2. **Initialize MongoDB Connection**: Connects to a MongoDB database and specifies the collection where the embeddings will be stored.

3. **Load Sentence Transformer Model**: Uses the `all-MiniLM-L6-v2` model from the `sentence-transformers` library to generate embeddings.

4. **Batch Processing**: Processes reviews in batches to efficiently handle large datasets. The batch size is set to 256 by default but can be adjusted based on system capabilities.

5. **Generate Embeddings**: For each batch, the script generates embeddings for the review text.

6. **Store in MongoDB**: The generated embeddings, along with the review text, are stored in the specified MongoDB collection.

7. **Completion Message**: Prints a success message once all embeddings are generated and stored.

## Execution

Run the script using Python:

```bash
python generate_embedding.py
```

Ensure that your MongoDB instance is running and accessible before executing the script.

## Notes

- Adjust the `batch_size` variable if you encounter memory issues or if your system can handle larger batches.
- The embeddings are stored as lists in MongoDB to ensure compatibility with MongoDB's data types.

This script is a tool for transforming text data into a format suitable for machine learning applications, leveraging the capabilities of modern NLP models.
```
