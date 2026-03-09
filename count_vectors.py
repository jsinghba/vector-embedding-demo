# Script to count the number of vectors in all_vectors.txt

file_path = 'all_vectors.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

num_vectors = len(lines)
print(f"Number of vectors in '{file_path}': {num_vectors}")
