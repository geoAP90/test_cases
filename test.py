# library_system_test.py

# The Library System Code
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self):
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Not Available'})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a new book to the library."""
        self.books.append(book)

    def search_by_title(self, title: str):
        """Search for books by title."""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str):
        """Search for books by author."""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def check_availability(self, title: str):
        """Check if a specific book is available."""
        for book in self.books:
            if title.lower() == book.title.lower():
                return book.available
        return False

    def total_books(self):
        """Return the total number of books in the library."""
        return len(self.books)


# Test Case Functions
def test_add_book():
    library = Library()
    book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books[0].title == "Harry Potter and the Philosopher's Stone"

def test_search_by_title():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)
    
    result = library.search_by_title("gatsby")
    assert len(result) == 1
    assert result[0].title == "The Great Gatsby"
    
    result = library.search_by_title("mockingbird")
    assert len(result) == 1
    assert result[0].title == "To Kill a Mockingbird"

def test_search_by_author():
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("Animal Farm", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    
    result = library.search_by_author("george orwell")
    assert len(result) == 2
    assert result[0].author == "George Orwell"
    assert result[1].author == "George Orwell"

def test_check_availability():
    library = Library()
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", True)
    book2 = Book("Pride and Prejudice", "Jane Austen", False)
    library.add_book(book1)
    library.add_book(book2)
    
    assert library.check_availability("The Catcher in the Rye") == True
    assert library.check_availability("Pride and Prejudice") == False
    assert library.check_availability("Non Existent Book") == False

def test_total_books():
    library = Library()
    book1 = Book("The Hobbit", "J.R.R. Tolkien")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    library.add_book(book1)
    library.add_book(book2)
    
    assert library.total_books() == 2

def test_search_no_results():
    library = Library()
    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book(book1)
    
    result = library.search_by_title("Moby Dick")
    assert len(result) == 0

# Main Function to Run Tests
def run_tests():
    print("Running tests...\n")
    
    test_add_book()
    print("test_add_book passed")
    
    test_search_by_title()
    print("test_search_by_title passed")
    
    test_search_by_author()
    print("test_search_by_author passed")
    
    test_check_availability()
    print("test_check_availability passed")
    
    test_total_books()
    print("test_total_books passed")
    
    test_search_no_results()
    print("test_search_no_results passed")
    
    print("\nAll tests passed!")

# Run the test suite
if __name__ == "__main__":
    run_tests()
