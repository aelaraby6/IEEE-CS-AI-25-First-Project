class Book:
    def __init__(self, book_id, title, author, publication_year, publisher):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.publisher = publisher

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}\nPublisher: {self.publisher}\n"

    
