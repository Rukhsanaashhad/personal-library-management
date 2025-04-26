import json

library = []

def display_menu():
    print("Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    search_choice = input("Enter your choice: ")
    if search_choice == "1":
        title = input("Enter the title: ")
        matching_books = [book for book in library if book["title"] == title]
    elif search_choice == "2":
        author = input("Enter the author: ")
        matching_books = [book for book in library if book["author"] == author]
    else:
        print("Invalid choice!")
        return
    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

def display_all_books():
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_statistics():
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read}%")

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)
    print("Library saved to file.")

def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
        print("Library loaded from file.")
    except FileNotFoundError:
        print("No saved library found.")

def main():
    load_library()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
