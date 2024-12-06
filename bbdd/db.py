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

    def __repr__(self):
        return(u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Book(db.Model):
    """Books of our application"""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120), nullable=False)
    description = Column(Text(250), nullable=True, default=None)

    CategoryID = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", backref="Books")
    
    def _re__(self):
        return(u'<{self.__class__.__name__}: {self.id}>'.format(self=self))