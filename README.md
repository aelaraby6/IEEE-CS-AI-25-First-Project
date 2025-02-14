# Library Management System

This is a Library Management System built using Python, which helps to manage books in a library. It allows users to perform operations like adding, updating, viewing, deleting books, and saving/loading book data from Excel or SQLite database.

## Features

- Add a new book to the library
- View all books in the library

![output](https://github.com/user-attachments/assets/e9ec75da-7131-4f05-9ede-b4d48c71ca0d)

- Search for a book by ID or Title
- Update book information
- Delete a book from the library
- Save and load books to/from an Excel file (`library.xlsx`)

![excel](https://github.com/user-attachments/assets/30eefda4-72d1-4e1c-ad57-7e16478f5022)

- Save and load books to/from an SQLite database (`library.db`)

## Libraries Used

This project uses the following Python libraries:

1. **pandas**:  
   - Used for working with data structures and reading/writing data to Excel files. The `pandas.DataFrame` is used to handle and manipulate the book data before saving or loading it from Excel.
   - Installation: `pip install pandas`

2. **tabulate**:  
   - Used to format the output of the list of books into a readable table format when viewing books in the console.
   - Installation: `pip install tabulate`

3. **openpyxl**:  
   - Used to work with Excel files, allowing the system to save book data to an Excel file and read data from it.
   - Installation: `pip install openpyxl`

4. **sqlite3**:  
   - A built-in Python library that provides an interface to SQLite databases, used to save and retrieve book data from the SQLite database (`library.db`).
   - Installation: Already included with Python (no need for extra installation).

5. **os**:  
   - Used to clear the console screen to keep the interface clean during operation.
   - This is a built-in Python library, so no installation is needed.

