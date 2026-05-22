from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    available: bool = True  # quita el espacio antes de ":"

    def summary(self) -> str:
        """Return a short human-readable description of the book."""
        return f"'{self.title}' by {self.author} has {self.pages} pages."


if __name__ == "__main__":
    book = Book(title="Clean Code", author="Robert Martin", pages=431)
    print(book.summary())