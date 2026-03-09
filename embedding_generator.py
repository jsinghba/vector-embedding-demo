# scripts/embedding_generator.py

from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    return model.encode(text)

def embed_documents(file_paths):
    embeddings = []
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            embedding = embed_text(content)
            embeddings.append(embedding)
    return np.array(embeddings)

if __name__ == "__main__":
    file_paths = [
        'data/ospf_doc.txt',
        'data/pasta_recipe.txt',
        'data/BGP_documentation.txt'
    ]
    embeddings = embed_documents(file_paths)
    # Save embeddings to disk
    with open('embeddings.pkl', 'wb') as f:
        pickle.dump(embeddings, f)
    print("Embeddings saved to embeddings.pkl")
