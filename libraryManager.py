from book import Book
import pandas as pd
from tabulate import tabulate
import data
import os  

# Add New Book
def addBook(library):
    try:
        os.system("cls" if os.name == "nt" else "clear")

        bookId = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        publicationYear = input("Enter Publication Year: ")
        publisher = input("Enter Publisher: ")

        if not bookId or not title or not author or not publicationYear or not publisher:
            print("Error: All fields must be filled in.")
            return

        newBook = Book(bookId, title, author, publicationYear, publisher)
        library.append(newBook)
        print("Book added successfully!")
        os.system("cls" if os.name == "nt" else "clear")
    
    except Exception as e:
        print(f"An unexpected error occurred while adding the book: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# Delete Book
def deleteBook(library):
    try:
        os.system("cls" if os.name == "nt" else "clear")

        if not library:
            print("There are no books to delete.")
            return

        deleteBookId = input("Enter the Book ID to delete: ")
        found = False
        
        for book in library:
            if str(book.getBookId()) == deleteBookId:
                library.remove(book)
                print("The book has been deleted.")
                found = True
                break
        
        if not found:
            print("The book was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred while deleting the book: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# Search about Book
def searchBook(library):
    try:
        os.system("cls" if os.name == "nt" else "clear")

        search = input("Enter Book ID or Title to search: ")
        found = False
        for book in library:
            if str(book.getBookId()) == search or book.getTitle().lower() == search.lower():
                book.displayBook()
                found = True
                break
        if not found:
            print("Book not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred while searching for the book: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# view Books
def viewBooks(library):
    try:
        os.system("cls" if os.name == "nt" else "clear")

        if not library:
            print("\nNo books available.")
        else:
            headers = ["Book ID", "Title", "Author", "Year", "Publisher"]
            data = [
                [book.getBookId(), book.getTitle(), book.getAuthor(), book.getPublicationYear(), book.getPublisher()]
                for book in library
            ]
        
            print(tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
    
    except Exception as e:
        print(f"An unexpected error occurred while viewing books: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# Update Book info
def updateBook(library):
    try:
        search = input("Enter Book ID or Title to search: ")
        found = False
        for book in library:
            if book.getBookId() == search or book.getTitle().lower() == search.lower():
                searchedBook = book
                found = True
                break
        if not found:
            print("Book not found.")
            return

        data.LibraryOptions.dataOptions()
        option = input("Enter the number of the attribute you want to update: ")
        key = data.attributes.get(option)
        if key:
            new_value = input(f"Enter the new value for {key}: ")

            if key == "bookId":
                searchedBook.setBookId(new_value)  
            elif key == "title":
                searchedBook.setTitle(new_value)
            elif key == "author":
                searchedBook.setAuthor(new_value)
            elif key == "publicationYear":
                searchedBook.setPublicationYear(new_value)   
            elif key == "publisher":
                searchedBook.setPublisher(new_value)

            os.system("cls" if os.name == "nt" else "clear")
            print("\nBook updated successfully!")
        else:
            print("Invalid option. Please try again.")
            os.system("cls" if os.name == "nt" else "clear")
    
    except Exception as e:
        print(f"An unexpected error occurred while updating the book: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# Save books to Excel
def saveBookstoExcel(library):
    try:
        data = {
            "bookId": [book.getBookId() for book in library],
            "title": [book.getTitle() for book in library],
            "author": [book.getAuthor() for book in library],
            "publicationYear": [book.getPublicationYear() for book in library],
            "publisher": [book.getPublisher() for book in library]
        }

        df = pd.DataFrame(data)
        df.to_excel("library.xlsx", index=False)
        print("Books saved to library.xlsx successfully!")
        os.system("cls" if os.name == "nt" else "clear")
    
    except Exception as e:
        print(f"An unexpected error occurred while saving books to Excel: {e}")
        os.system("cls" if os.name == "nt" else "clear")

# Load from Excel sheet
def loadBooksfromExcel(library):
    try:
        df = pd.read_excel("library.xlsx")

        if df.empty:
            print("The file is empty. No books to load.")
            os.system("cls" if os.name == "nt" else "clear")
            return

        required_columns = ["bookId", "title", "author", "publicationYear", "publisher"]
        if not all(col in df.columns for col in required_columns):
            print("The Excel file is missing some required columns.")
            os.system("cls" if os.name == "nt" else "clear")
            return

        for _, row in df.iterrows():
            book = Book(row["bookId"], row["title"], row["author"], row["publicationYear"], row["publisher"])
            library.append(book)

        print("Books loaded from library.xlsx successfully!")
        os.system("cls" if os.name == "nt" else "clear")
    
    except FileNotFoundError:
        print("No data found: The file 'library.xlsx' does not exist.")
        os.system("cls" if os.name == "nt" else "clear")
    
    except ValueError:
        print("Error: The Excel file contains invalid data. Please check the format.")
        os.system("cls" if os.name == "nt" else "clear")

    except Exception as e:
        print(f"An unexpected error occurred while loading books from Excel: {e}")
        os.system("cls" if os.name == "nt" else "clear")
