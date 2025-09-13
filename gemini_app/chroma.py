# services/chroma.py
import chromadb

# Pakai PersistentClient (menyimpan data ke folder ./chroma_db)
client = chromadb.PersistentClient(path="./chroma_db")

# Buat / ambil koleksi bernama "my_collection"
collection = client.get_or_create_collection("my_collection")

def add_to_chroma(documents, ids, metadatas=None, embeddings=None):
    print("Adding to Chroma:")
    print(f"  Documents: {documents}")
    print(f"  IDs: {ids}")
    print(f"  Metadatas: {metadatas}")
    # embeddings optional
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
        embeddings=embeddings
    )
    print("Successfully added to Chroma!")

def query_chroma(query_texts, n_results=3):
    return collection.query(query_texts=query_texts, n_results=n_results)
