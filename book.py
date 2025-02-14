class Book:
    count = 0  

    def __init__(self, bookId, title, author, publicationYear, publisher):
        self.__bookId = bookId
        self.__title = title
        self.__author = author
        self.__publicationYear = publicationYear
        self.__publisher = publisher
        Book.count += 1  
        self.__bookNumber = Book.count  

    def getBookId(self):
        return self.__bookId
    
    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getPublicationYear(self):
        return self.__publicationYear
    
    def getPublisher(self):
        return self.__publisher
    
    def setBookId(self, bookId):
        self.__bookId = bookId
    
    def setTitle(self, title):
        self.__title = title
    
    def setAuthor(self, author):
        self.__author = author
    
    def setPublicationYear(self, publicationYear):
        self.__publicationYear = publicationYear
    
    def setPublisher(self, publisher):
        self.__publisher = publisher
    