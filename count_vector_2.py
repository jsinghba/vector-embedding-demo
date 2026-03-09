# Count total number of values across all vectors
file_path = 'all_vectors.txt'

total_values = 0
with open(file_path, 'r') as f:
    for line in f:
        total_values += len(line.strip().split())

print(f"Total number of values in the file: {total_values}")
