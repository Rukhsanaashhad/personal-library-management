import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Simple Library", layout="wide")

# Session State Initialization
if "library" not in st.session_state:
    st.session_state.library = []

# Load and Save Functions
def load_library():
    if os.path.exists("library.json"):
        with open("library.json", "r") as file:
            st.session_state.library = json.load(file)

def save_library():
    with open("library.json", "w") as file:
        json.dump(st.session_state.library, file)

# Add Book Function
def add_book(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "added": datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.library.append(book)
    save_library()

# Remove Book Function
def remove_book(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()

# Load Library Data
load_library()

# Sidebar Navigation
page = st.sidebar.selectbox("Select a page", ["View Library", "Add Book"])

# Main Title
st.title("📚 Simple Personal Library")

# Add Book Page
if page == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=datetime.now().year, value=2024)
    
    if st.button("Add Book"):
        if title and author:
            add_book(title, author, year)
            st.success("Book added successfully!")
        else:
            st.warning("Please enter both title and author")

# View Library Page
elif page == "View Library":
    st.subheader("Your Library")
    
    if not st.session_state.library:
        st.info("Library is empty. Add some books!")
    else:
        for i, book in enumerate(st.session_state.library):
            st.write(f"### {book['title']}")
            st.write(f"Author: {book['author']}")
            st.write(f"Year: {book['year']}")
            st.write(f"Added: {book['added']}")
            if st.button("Remove", key=f"remove_{i}"):
                remove_book(i)
                st.experimental_rerun()
