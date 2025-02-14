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
            libraryManager.updateBook(library)
        elif choice == "5":
            libraryManager.deleteBook(library)
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
