from typing import Optional, List


class Book:
    """Represents a book with title, author and checkout state."""
def __init__(self):
    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self._is_checked_out: bool = False

    def check_out(self) -> bool:
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    @property
    def is_available(self) -> bool:
        """True if the book is not checked out."""
        return not self._is_checked_out

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, available={self.is_available})"


class Library:
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book instance to the library."""
        self._books =[]

    def _find_book_by_title(self, title: str) -> Optional[Book]:
        """Return the first Book matching title or None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str) -> bool:
        """
        Attempt to check out a book by title.
        Returns True if successful, False if book not found or already checked out.
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.check_out()
    def return_book(self, title: str) -> bool:
        """
        Attempt to return a book by title.
        Returns True if successful, False if book not found or wasn't checked out.
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self) -> List[Book]:
        """Return a list of available (not checked out) Book instances."""
        return [book for book in self._books if book.is_available]