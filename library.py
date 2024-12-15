from flask import Flask, abort, render_template, request, redirect
import config
from bbdd.db import Book, Category, Author, State, BookAuthor, db
from forms.library_forms import BookForm, AuthorForm

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bookshelf/')
def list_books():
    books = Book.query.all()
    return render_template('bookshelf.html', books=books)

@app.route('/authors/')
def list_authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

@app.route('/book/<int:id>/')
def view_book_details(id):
    book = Book.query.filter_by(id=id).first()

    if book:
        return render_template('book_details.html', book=book)
    else:
        abort(404)

@app.route('/author/<int:id>/')
def view_author_details(id):
    author = Author.query.filter_by(id=id).first()

    if author:
        return render_template('author_details.html', author=author)
    else:
        abort(404)

@app.route('/book/<int:id>/delete/')
def delete_book(id):
    book = Book.query.filter_by(id=id).first()
    BookAuthor.query.filter_by(book_id=book.id).delete()
    db.session.delete(book)
    db.session.commit()
    return redirect('/bookshelf')

@app.route('/author/<int:id>/delete/')
def delete_author(id):
    author = Author.query.filter_by(id=id).first()
    BookAuthor.query.filter_by(author_id=author.id).delete()
    db.session.delete(author)
    db.session.commit()
    return redirect('/authors')

@app.route('/book/create/', methods=["get","post"])
def create_book():
    form = BookForm(request.form)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    form.state_id.choices = [(state.id, state.name) for state in State.query.all()]

    if form.validate() and request.method == "POST":
        new_book = Book()
        new_book.title = form.title.data
        new_book.description = form.description.data
        new_book.CategoryID = form.category_id.data
        new_book.StateID = form.state_id.data
        new_book.image = form.image.data
        
        db.session.add(new_book)
        db.session.commit()

        selected_authors = form.author.data
        for author_id in selected_authors:
            book_author = BookAuthor(book_id=new_book.id, author_id=author_id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/bookshelf/')

    return render_template('create_book_form.html', form=form)

@app.route('/author/create/', methods=["get","post"])
def create_author():
    form = AuthorForm(request.form)

    form = AuthorForm(request.form)
    form.book.choices = [(book.id, book.title) for book in Book.query.all()]

    if form.validate() and request.method == "POST":
        new_author = Author()
        new_author.name = form.name.data
        new_author.biography = form.biography.data
        new_author.image = form.image.data
        
        db.session.add(new_author)
        db.session.commit()

        selected_books = form.book.data
        for book_id in selected_books:
            book_author = BookAuthor(book_id=book_id, author_id=new_author.id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/authors/')

    return render_template('create_author_form.html', form=form)

@app.route('/book/<int:id>/update/', methods=["get","post"])
def update_book(id):
    book = Book.query.filter_by(id=id).first()

    form = BookForm(request.form, obj=book)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    form.state_id.choices = [(state.id, state.name) for state in State.query.all()]

    if form.validate() and request.method == "POST":
        book.title = form.title.data
        book.description = form.description.data
        book.author = form.author.data
        book.CategoryID = form.category_id.data
        book.StateID = form.state_id.data
        book.image = form.image.data

        BookAuthor.query.filter_by(book_id=book.id).delete()

        selected_authors = form.author.data
        for author_id in selected_authors:
            book_author = BookAuthor(book_id=book.id, author_id=author_id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/bookshelf/')
    
    current_authors = [author.author_id for author in book.book_authors]
    form.author.data = current_authors

    return render_template('update_book_form.html', book=book, form=form)

@app.route('/author/<int:id>/update/', methods=["get","post"])
def update_author(id):
    author = Author.query.filter_by(id=id).first()

    form = AuthorForm(request.form, obj=author)
    form.book.choices = [(book.id, book.title) for book in Book.query.all()]

    if form.validate() and request.method == "POST":
        author.name = form.name.data
        author.biography = form.biography.data
        author.image = form.image.data

        selected_books = form.book.data 
        BookAuthor.query.filter_by(author_id=author.id).delete()
        for book_id in selected_books:
            book_author = BookAuthor(book_id=book_id, author_id=author.id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/authors/')
    
    current_books = [book_author.book_id for book_author in author.book_authors]
    form.book.data = current_books

    return render_template('update_author_form.html', author=author, form=form)