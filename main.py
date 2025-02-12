from book import Book
import os  


# main menu
def menu():
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book Details")
        print("5. Delete Book")
        print("6. Exit")
        

def main():
    library = []  # List to store books
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        print(f"\n")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            publication_year = input("Enter Publication Year: ")
            publisher = input("Enter Publisher: ")
            
            new_book = Book(book_id, title, author, publication_year, publisher)
            library.append(new_book)
            print("Book added successfully!")
            os.system("cls" if os.name == "nt" else "clear")

        
        elif choice == "2":
            if not library:
                print("No books available.")
            else:
                for book in library:
                    book.display_book() 
        
        elif choice == "3":
            search = input("Enter Book ID or Title to search: ")
            found = False
            for book in library:
                if book.book_id == search or book.title.lower() == search.lower():
                    book.display_book()
                    found = True
                    break
            if not found:
                print("Book not found.")
        elif choice == "4":
            # Update book logic here
            pass
        elif choice == "5":
                    elif choice == "5":
            if not library:
                print("There are no books to delete")
            else:
                delete_id = input("Enter the book id: ")
                found = False
                for book in library:
                    if book.book_id == delete_id:
                        library.remove(book)
                        print("The book has been deleted")
                        found = True
                        break
                if not found:
                    print("The book was not found")

            pass
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
