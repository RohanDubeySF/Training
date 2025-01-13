# Create a class Book that keeps track of the number of books created. Implement a class method get_book_count() that returns the total number of books created. Additionally, implement an instance method display_info() that prints the title and author of the book.

class Book():
    no=0
    def __init__(self):
        Book.no+=1
    
    def display_info(self,Title,Author):
        self.Title=Title
        self.Author=Author
        print(f"Title {self.Title} by {self.Author}")

    @classmethod
    def book_count(cls):
        return cls.no

b1=Book()
b2=Book()
b3=Book()    
b1.display_info("1984", "George Orwell")  # Output: Title: 1984, Author: George Orwell
b2.display_info("To Kill a Mockingbird", "Harper Lee")  # Output: Title: To Kill a Mockingbird, Author: Harper Lee
b3.display_info("The Great Gatsby", "F. Scott Fitzgerald")  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald

# Getting the total number of books created
print(Book.book_count())  # Output: 3