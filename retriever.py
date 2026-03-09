import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load your FAISS index
index = faiss.read_index('my_faiss_index.index')

# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # or your preferred model

# Your test question
question = "What DR stands for?"

# Generate embedding for the question
question_embedding = model.encode(question)
question_vector = np.array(question_embedding, dtype='float32').reshape(1, -1)

# Search for top 3 similar vectors
k = 3
distances, indices = index.search(question_vector, k)

print(f"Question: {question}")
print("Most similar vectors:")
for i in range(k):
    print(f"Index: {indices[0][i]}, Distance: {distances[0][i]}")
