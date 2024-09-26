from typing import List
from docx import Document
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class DocxIngestor(IngestorInterface):
    """Concrete ingestor for DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX files and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with extension: {path}")

        quotes = []
        try:
            doc = Document(path)
            for para in doc.paragraphs:
                if para.text:
                    try:
                        body, author = para.text.strip().split(' - ')
                        quotes.append(QuoteModel(body.strip(), author.strip()))
                    except ValueError:
                        pass  # Skip paragraphs that don't match the expected format
        except Exception as e:
            raise Exception(f"Error reading DOCX file: {path}") from e
        return quotes