from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
import os

class Ingestor(IngestorInterface):
    """A unified interface to ingest quotes from various file types."""

    ingestors = [TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate ingestor and parse the file."""

        # Ensure the path is absolute
        path = os.path.abspath(path)
        
        # Check if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                if quotes is None:
                    raise ValueError(f"Ingestor {ingestor.__name__} returned None for file: {path}")
                return quotes

        raise ValueError(f"No suitable ingestor found for file: {path}")