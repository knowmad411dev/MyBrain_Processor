import logging
import chromadb
from chromadb.utils import embedding_functions
from embedding_model import EmbeddingModel
import os


class LLMClient:
    """
    Manages interactions with the Language Learning Model (LLM) and the Chroma vector database.

    Responsibilities:
        - Initialize and configure the Chroma vector store.
        - Generate embeddings using a custom PyTorch model.
        - Provide utility functions for text tokenization and LLM interactions.
    """

    def __init__(self, config):
        """
        Initialize the LLM client with the provided configuration.

        Args:
            config (Config): Configuration object containing settings.
        """
        self.config = config
        self.vector_store = self._initialize_vector_store()
        self.embedding_model = EmbeddingModel()

    def _initialize_vector_store(self):
        """
        Initialize and configure the Chroma vector store for managing embeddings.

        Returns:
            chromadb.Collection: Chroma collection instance for storing and querying embeddings.

        Logs:
            - Error: If initialization fails.
        """
        try:
            client = chromadb.Client()
            embedding_function = embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.getenv("OPENAI_API_KEY")
            )
            collection = client.get_or_create_collection(
                name="notes_collection",
                embedding_function=embedding_function
            )
            logging.info("Successfully initialized Chroma vector store.")
            return collection
        except Exception as e:
            logging.error(f"Failed to initialize Chroma vector store: {e}")
            return None

    def save_embedding(self, document: str, metadata: dict, doc_id: str) -> None:
        """
        Save a document's embedding to the Chroma vector store.

        Args:
            document (str): The document text to generate an embedding for.
            metadata (dict): Metadata to associate with the document.
            doc_id (str): A unique identifier for the document.

        Logs:
            - Info: When an embedding is successfully saved.
            - Error: If saving to the vector store fails.
        """
        try:
            embedding = self.embedding_model.generate_embedding(document, metadata).tolist()
            self.vector_store.add(
                documents=[document],
                metadatas=[metadata],
                ids=[doc_id],
                embeddings=[embedding]
            )
            logging.info(f"Successfully saved embedding for document ID: {doc_id}")
        except Exception as e:
            logging.error(f"Error saving embedding for document ID {doc_id}: {e}")
