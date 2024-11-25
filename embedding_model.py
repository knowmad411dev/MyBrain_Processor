from sentence_transformers import SentenceTransformer
import logging
import torch


class EmbeddingModel:
    """
    A wrapper for a pretrained SentenceTransformer embedding model.

    Methods:
        generate_embedding(text, metadata): Generates an embedding for input text with metadata.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", device: str = None):
        """
        Initialize the embedding model with lazy loading.

        Args:
            model_name (str): Name of the pretrained model.
            device (str): Device to use for inference ('cpu' or 'cuda'). If None, defaults to auto-detection.
        """
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = None  # Lazy loading
        logging.info(f"EmbeddingModel initialized with model '{self.model_name}' on device '{self.device}'.")

    def load_model(self):
        """
        Load the SentenceTransformer model when needed.
        """
        if self.model is None:
            logging.info("Loading SentenceTransformer model...")
            self.model = SentenceTransformer(self.model_name, device=self.device)
            logging.info("Model loaded successfully.")

    def generate_embedding(self, text: str, metadata: dict):
        """
        Generate an embedding for the given text and metadata.

        Args:
            text (str): Input text or code for embedding generation.
            metadata (dict): Metadata to include in the embedding context.

        Returns:
            List[float]: The generated embedding vector.
        """
        self.load_model()

        # Combine metadata with text for embedding context
        context = f"Metadata: {metadata}\nContent: {text}"
        return self.model.encode(context)
