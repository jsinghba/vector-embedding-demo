import pickle
import numpy as np

# Load the embeddings
with open('embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)

# Save all vectors to a text file
with open('all_vectors.txt', 'w') as f:
    for vector in embeddings:
        # Convert each vector to a string of space-separated values
        vector_str = ' '.join(map(str, vector))
        f.write(vector_str + '\n')

print("All vectors saved to 'all_vectors.txt'")
