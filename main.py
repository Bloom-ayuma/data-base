from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List

# FastAPI application instance
app = FastAPI()

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "library_system"
}

# Establishing database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Pydantic models for validation
class Book(BaseModel):
    Title: str
    Author: str
    ISBN: str
    PublishedYear: int
    Genre: str

class Member(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    PhoneNumber: str
    MembershipDate: str

class Loan(BaseModel):
    BookID: int
    MemberID: int
    LoanDate: str
    ReturnDate: str

# 1. CRUD Operations for Books

@app.post("/books/")
def create_book(book: Book):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Books (Title, Author, ISBN, PublishedYear, Genre)
        VALUES (%s, %s, %s, %s, %s)
    """, (book.Title, book.Author, book.ISBN, book.PublishedYear, book.Genre))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Book added successfully"}

@app.get("/books/{book_id}")
def read_book(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Books WHERE BookID = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Books SET Title = %s, Author = %s, ISBN = %s, PublishedYear = %s, Genre = %s
        WHERE BookID = %s
    """, (book.Title, book.Author, book.ISBN, book.PublishedYear, book.Genre, book_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE BookID = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Book deleted successfully"}

# 2. CRUD Operations for Members
# Similarly, you can define CRUD operations for Members and Loans

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
