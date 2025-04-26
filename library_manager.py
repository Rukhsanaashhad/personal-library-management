import json  
import streamlit as st  

# Initialize library  
library = []  

# Load library from file if it exists  
def load_library():  
    global library  
    try:  
        with open("library.txt", "r") as file:  
            library = json.load(file)  
    except FileNotFoundError:  
        library = []  
        st.warning("No saved library found. Start adding books!")  

# Save library to file  
def save_library():  
    with open("library.txt", "w") as file:  
        json.dump(library, file)  
    st.success("Library saved to file.")  

load_library()  

# Display menu options  
st.title("Personal Library Manager")  

# Add a book  
if st.sidebar.button("Add a Book"):  
    st.header("Add a New Book")  
    title = st.text_input("Book Title")  
    author = st.text_input("Author")  
    year = st.number_input("Publication Year", min_value=0, step=1)  
    genre = st.text_input("Genre")  
    read = st.checkbox("Have you read this book?")  
    
    if st.button("Submit"):  
        book = {  
            "title": title,  
            "author": author,  
            "year": year,  
            "genre": genre,  
            "read": read  
        }  
        library.append(book)  
        st.success("Book added successfully!")  

# Remove a book  
if st.sidebar.button("Remove a Book"):  
    st.header("Remove a Book")  
    title_to_remove = st.text_input("Enter the title of the book to remove")  
    
    if st.button("Remove"):  
        for book in library:  
            if book["title"] == title_to_remove:  
                library.remove(book)  
                st.success("Book removed successfully!")  
                break  
        else:  
            st.error("Book not found!")  

# Search for a book  
if st.sidebar.button("Search for a Book"):  
    st.header("Search for a Book")  
    search_choice = st.selectbox("Search by:", ["Title", "Author"])  
    
    if search_choice == "Title":  
        title_to_search = st.text_input("Enter the title")  
    else:  
        author_to_search = st.text_input("Enter the author")  
    
    if st.button("Search"):  
        if search_choice == "Title":  
            matching_books = [book for book in library if book["title"] == title_to_search]  
        else:  
            matching_books = [book for book in library if book["author"] == author_to_search]  
        
        if matching_books:  
            st.subheader("Matching Books:")  
            for book in matching_books:  
                st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")  
        else:  
            st.warning("No matching books found.")  

# Display all books  
if st.sidebar.button("Display All Books"):  
    st.header("Your Library")  
    if not library:  
        st.warning("Your library is empty.")  
    else:  
        for i, book in enumerate(library, 1):  
            st.write(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")  

# Display statistics  
if st.sidebar.button("Display Statistics"):  
    st.header("Library Statistics")  
    total_books = len(library)  
    read_books = sum(book["read"] for book in library)  
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0  
    
    st.write(f"Total books: {total_books}")  
    st.write(f"Percentage read: {percentage_read:.2f}%")  

# Save library on exit  
if st.sidebar.button("Save Library"):  
    save_library()  
