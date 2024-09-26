import pandas as pd
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class CSVIngestor(IngestorInterface):
    """Concrete ingestor for CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV files and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with extension: {path}")

        quotes = []
        try:
            df = pd.read_csv(path, header=0)
            for _, row in df.iterrows():
                if 'body' in row and 'author' in row:
                    quotes.append(QuoteModel(str(row['body']).strip(), str(row['author']).strip()))
        except Exception as e:
            raise Exception(f"Error reading CSV file: {path}") from e
        return quotes