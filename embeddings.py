from langchain_huggingface import HuggingFaceEmbeddings
model_name = "sentence-transformers/all-mpnet-base-v2"
huggingface_embeddings = HuggingFaceEmbeddings(model_name=model_name)
