from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class for all file ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if the file type is compatible with the ingestor class."""
        ext = path.split('.')[-1]
        return ext.lower() in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and return a list of QuoteModel objects."""
        pass

    @classmethod
    def verify_can_ingest(cls, path: str):
        """Verify if the file can be ingested, else raise an error."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with extension: {path}")