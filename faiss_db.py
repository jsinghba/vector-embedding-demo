import faiss
import numpy as np

# Step 1: Load vectors from your text file
vectors = []

with open('all_vectors.txt', 'r') as f:
    for line in f:
        vector = list(map(float, line.strip().split()))
        vectors.append(vector)

# Convert to numpy array
vector_array = np.array(vectors).astype('float32')

# Step 2: Create FAISS index
dimension = vector_array.shape[1]
index = faiss.IndexFlatL2(dimension)  # Using L2 distance
index.add(vector_array)

# Step 3: Save the index to disk
faiss.write_index(index, 'my_faiss_index.index')

print(f"Index saved successfully with {index.ntotal} vectors.")
