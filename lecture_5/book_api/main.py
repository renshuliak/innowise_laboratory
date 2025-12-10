
"""
Book Collection API

A FastAPI application that manages a book collection with CRUD operations,
search functionality, and database integration using SQLAlchemy.
"""

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional

from database import get_db, engine, Base
from models import Book
from schemas import BookCreate, BookUpdate, BookResponse

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Book Collection API", version="1.0.0")


@app.post("/books/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the collection"""
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """Get all books in the collection"""
    books = db.query(Book).all()
    return books


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    """Update book details"""
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update only provided fields
    update_data = book_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return None


@app.get("/books/search/", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None, description="Search by title"),
    author: Optional[str] = Query(None, description="Search by author"),
    year: Optional[int] = Query(None, description="Search by year"),
    db: Session = Depends(get_db)
):
    """Search books by title, author, or year"""
    query = db.query(Book)
    
    filters = []
    if title:
        filters.append(Book.title.ilike(f"%{title}%"))
    if author:
        filters.append(Book.author.ilike(f"%{author}%"))
    if year:
        filters.append(Book.year == year)
    
    if filters:
        query = query.filter(or_(*filters))
    
    books = query.all()
    return books


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to Book Collection API", "docs": "/docs"}

