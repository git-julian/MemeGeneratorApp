import subprocess
import os
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """Concrete ingestor for PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF files using pdftotext CLI and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with extension: {path}")

        quotes = []
        tmp = f'./{os.path.basename(path).split(".")[0]}.txt'
        try:
            subprocess.run(['pdftotext', '-layout', path, tmp], check=True)
            with open(tmp, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        try:
                            body, author = line.split(' - ')
                            quotes.append(QuoteModel(body.strip(), author.strip()))
                        except ValueError:
                            pass  # Skip lines that don't match the expected format
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error converting PDF file: {path}") from e
        except FileNotFoundError:
            raise Exception("pdftotext not found. Please install it.")
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
        return quotes