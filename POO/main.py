
loan_history_books = []

class Book:
    
    def __init__(self, title, author, category, isbn, available=True):
        self.title = title
        self.author = author
        self.available = available
        self.category = category
        self.isbn = isbn
        self.__amount_loans = 0
        
    def __str__(self):
        return f"{self.title} by {self.author} ----> available: {self.available} ----> ISBN: {self.isbn} ----> category: {self.category}"

    def lend(self):
        if self.available:
            self.available = False
            self.__amount_loans += 1
            return f"{self.title} was lend successfuly. Totally loans: {self.__amount_loans}"
        return f"{self.title} is not avalible"
    
    def return_book(self):
        self.available = True
        return f"{self.title} was returned successfuly"
    
    def is_popular(self):
        return self.__amount_loans > 5
    
    def get_amount_loans(self):
        return self.__amount_loans

    def set_amount_loans(self, amount_loans):
        self.__amount_loans = amount_loans

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Science Fiction", "1234567890", True)
other_book = Book("1984", "George Orwell", "Science Fiction", "1234567890", True)


my_book.set_amount_loans(10)
print(my_book.get_amount_loans())

print(my_book.lend())
print(my_book.lend())
print(my_book.return_book())

catalog = [my_book, other_book]

for book in catalog:
    print(book)

