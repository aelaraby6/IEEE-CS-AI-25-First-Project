from book import Book
import libraryManager
import database
import data

def main():
    global book
    library = [] 
    
    while True:
        data.LibraryOptions.menu()
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            libraryManager.addBook(library)
        
        elif choice == "2":
            libraryManager.viewBooks(library)
        
        elif choice == "3":
            libraryManager.searchBook(library)
        
        elif choice == "4":
            # Update book logic here
             title_or_id = input("Would you like to update (1) Book ID or (2) Title? Enter 1 or 2: ")

                if title_or_id == "1":
                    current_id = input("Enter the current Book ID you want to update: ")
                    found = False
                    for book in library:
                        if book.get_book_id() == current_id:
                            found = True
                            new_id = input("Enter the new Book ID to replace the old one: ")
                            book.set_book_id(new_id)
                            print(f"Book ID updated successfully!")
                            break
                    if not found:
                        print("Book not found.")

                elif title_or_id == "2":
                    current_title = input("Enter the current Book Title you want to update: ")
                    found = False
                    for book in library:
                        if book.get_title().lower() == current_title.lower():
                            found = True
                            new_title = input("Enter the new Book Title to replace the old one: ")
                            book.set_title(new_title)
                            print(f"Book Title updated successfully!")
                            break
                    if not found:
                        print("Book not found.")

                else:
                    print("Invalid choice! Please enter 1 or 2.")
            pass
        elif choice == "5":
            # Delete book logic here
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
            database.saveBookstoDB(library)
        
        elif choice == "7":
            database.loadBooksfromDb(library)
        
        elif choice == "8":
            libraryManager.save_books_to_excel(library)
        
        elif choice == "9":
            libraryManager.load_books_from_excel(library)
        
        elif choice == "10":
            print("Exiting the system")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-10.")

if __name__ == "__main__":
    main()
