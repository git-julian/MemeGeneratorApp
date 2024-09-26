from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor for text files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the text file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file: {path}")
        
        quotes = []
        try:
            with open(path, 'r') as file:
                for line in file.readlines():
                    # Assuming the text file format is "quote - author"
                    line = line.strip()
                    if len(line) > 0:
                        parse = line.split(' - ')
                        if len(parse) == 2:
                            new_quote = QuoteModel(parse[0], parse[1])
                            quotes.append(new_quote)
        except Exception as e:
            print(f"Error while reading the file: {e}")
            return None

        return quotes