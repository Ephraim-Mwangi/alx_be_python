class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = num_pages

class Library:
    def __init__(self):
        self.books = []  # List to store instances of Book, EBook, and PrintBook
        
    def add_book(self, book):
        # Check if the book is an instance of Book or its subclasses
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Can only add Book, EBook, or PrintBook instances")
            
    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
            
        print("\nLibrary Books:")
        for book in self.books:
            # Print common attributes
            print(f"\nTitle: {book.title}")
            print(f"Author: {book.author}")
            
            # Print specific attributes based on book type
            if isinstance(book, EBook):
                print(f"Type: E-Book")
                print(f"File Size: {book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"Type: Print Book")
                print(f"Number of Pages: {book.num_pages}")
            else:
                print("Type: Book")
    def __init__(self):
        self.books = []  # List to store instances of Book, EBook, and PrintBook
        
    def add_book(self, book):
        # Check if the book is an instance of Book or its subclasses
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Can only add Book, EBook, or PrintBook instances")
            
    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
            
        print("\nLibrary Books:")
        for book in self.books:
            # Print common attributes
            print(f"\nTitle: {book.title}")
            print(f"Author: {book.author}")
            
            # Print specific attributes based on book type
            if isinstance(book, EBook):
                print(f"Type: E-Book")
                print(f"File Size: {book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"Type: Print Book")
                print(f"Number of Pages: {book.num_pages}")
            else:
                print("Type: Book")

