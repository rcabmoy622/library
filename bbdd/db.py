import datetime
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Category(db.Model):
    """Categories of books"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


class Book(db.Model):
    """Books of our application"""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120), nullable=False)
    description = Column(Text(250), nullable=True, default=None)
    CategoryID = Column(Integer, ForeignKey('categories.id'), nullable=False)
    StateID = Column(Integer, ForeignKey('states.id'), nullable=False)

    category = relationship("Category", backref="books")
    state = relationship("State", backref="books")


class Author(db.Model):
    """Authors of our application"""
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    biography = Column(Text, nullable=True)


class BookAuthor(db.Model):
    __tablename__ = 'book_authors'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), primary_key=True)

    book = relationship("Book", backref="book_authors")
    author = relationship("Author", backref="book_authors")


class State(db.Model):
    """States of our application"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)