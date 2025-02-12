class Book:
    count = 0  # Static variable to track book count
    
    def __init__(self, book_id, title, author, publication_year, publisher):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__publisher = publisher
        Book.count += 1  # Increment count when a new book is created
        self.__book_number = Book.count  # Assign book number
    
    # Getters
    def get_book_id(self):
        return self.__book_id
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publication_year(self):
        return self.__publication_year
    
    def get_publisher(self):
        return self.__publisher
    
    # Setters
    def set_book_id(self, book_id):
        self.__book_id = book_id
    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_publication_year(self, publication_year):
        self.__publication_year = publication_year
    
    def set_publisher(self, publisher):
        self.__publisher = publisher
    
    def display_book(self):
        print(f"======= Book {self.__book_number} =======")
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\nAuthor: {self.__author}\nYear: {self.__publication_year}\nPublisher: {self.__publisher}\n")
    