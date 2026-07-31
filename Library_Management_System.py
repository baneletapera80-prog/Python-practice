library = []

def add_book(title, author, year, book_id, availability):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "book ID": book_id,
        "availability": availability
    }
    library.append(book)

def view_books():
    if not library:
        print("No books in the library.")
        return
    for index, book in enumerate(library, start=1):
        print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Book ID: {book['book ID']}, Availability: {book['availability']}")

def search_book(query):
    found_books = [book for book in library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    if not found_books:
        print("No matching books found.")
        return
    print("\nSearch Results:")
    for index, book in enumerate(found_books, start=1):
        print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Book ID: {book['book ID']}, Availability: {book['availability']}")

def update_book(index, title, author, year, book_id, availability):
    if index < 1 or index > len(library):
        print("Invalid book index.")
        return
    library[index - 1] = {
        "title": title,
        "author": author,
        "year": year,
        "book ID": book_id,
        "availability": availability
    }
    print("Book updated successfully.")

def borrow_book(index):
    if index < 1 or index > len(library):
        print("Invalid book index.")
        return
    book = library[index - 1]
    print(f"You have borrowed '{book['title']}' by {book['author']}.")

def return_book(index):
    if index < 1 or index > len(library):
        print("Invalid book index.")
        return
    book = library[index - 1]
    print(f"You have returned '{book['title']}' by {book['author']}.")

def delete_book(index):
    if index < 1 or index > len(library):
        print("Invalid book index.")
        return
    book = library.pop(index - 1)
    print(f"Book '{book['title']}' by {book['author']} has been deleted from the library.") 

def save_to_books_file():
    with open('books.txt', 'w') as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['book ID']},{book['availability']}\n")
    print("Library data saved to books.txt.")
    with open('books.txt', 'w') as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['book ID']},{book['availability']}\n")
print("Library data saved to books.txt.")

def load_from_books_file():
    try:
        with open('books.txt', 'r') as file:
            for line in file:
                title, author, year, book_id, availability = line.strip().split(',')
                library.append({"title": title, "author": author, "year": year, "book ID": book_id, "availability": availability})
        print("Library data loaded from books.txt.")
    except FileNotFoundError:
        print("No saved library data found.")
try:
        with open('books.txt', 'r') as file:
            for line in file:
                title, author, year, book_id, availability = line.strip().split(',')
                library.append({"title": title, "author": author, "year": year, "book ID": book_id, "availability": availability})
        print("Library data loaded from books.txt.")
except FileNotFoundError:
        print("No saved library data found.")

def main():
    load_from_books_file()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Delete Book")
        print("8. Save and Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            book_id = input("Enter book ID: ")
            availability = input("Enter book availability: ")
            add_book(title, author, year, book_id, availability)
            print("Book added successfully.")
        elif choice == '2':
            view_books()
        elif choice == '3':
            query = input("Enter book title or author to search: ")
            search_book(query)
        elif choice == '4':
            view_books()
            index = int(input("Enter the number of the book to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new year: ")
            book_id = input("Enter new book ID: ")
            availability = input("Enter new availability: ")
            update_book(index, title, author, year, book_id, availability)
        elif choice == '5':
            view_books()
            index = int(input("Enter the number of the book to borrow: "))
            borrow_book(index)
        elif choice == '6':
            view_books()
            index = int(input("Enter the number of the book to return: "))
            return_book(index)
        elif choice == '7':
            view_books()
            index = int(input("Enter the number of the book to delete: "))
            delete_book(index)
        elif choice == '8':
            save_to_books_file()
            print("Exiting the system. Goodbye!")

if __name__ == "__main__":
    main()  