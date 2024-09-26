class QuoteModel:
    """A class to encapsulate a quote with body and author."""

    def __init__(self, body: str, author: str):
        """Initialize a quote object with a body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return a string representation of the quote."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Return a formal string representation of the quote."""
        return f'QuoteModel(body={self.body!r}, author={self.author!r})'