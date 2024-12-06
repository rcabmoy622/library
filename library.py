from flask import Flask, abort, render_template, request, redirect
import config
from bbdd.db import Book, Category, db
from forms.library_forms import BookForm

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bookshelf/')
def list():
    books = Book.query.all()
    return render_template('bookshelf.html', books=books, new_book = books)

@app.route('/book/<int:id>/')
def view_details(id):
    book = Book.query.filter_by(id=id).first()

    if book:
        return render_template('details.html', book=book)
    else:
        abort(404)

@app.route('/book/<int:id>/delete/')
def delete(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/list')

@app.route('/book/<int:id>/update/', methods=["get","post"])
def update(id):
    book = Book.query.filter_by(id=id).first()

    form = BookForm(request.form, obj=book)
    form.category_id.choices = [(categories.id, categories.name) for categories in Category.query.all()]

    if form.validate() and request.method == "POST":
        book.name = form.name.data
        book.description = form.description.data
        book.due_date = form.due_date.data
        book.reminder  = form.reminder.data
        book.CategoryID = form.category_id.data

        db.session.commit()

        return redirect('/list')

    return render_template('book_form.html', book=book, form=form)

@app.route('/book/create/', methods=["get","post"])
def create():
    form = BookForm(request.form)
    form.category_id.choices = [(categories.id, categories.name) for categories in Category.query.all()]

    if form.validate() and request.method == "POST":
        new_task = Book()
        new_task.title = form.title.data
        new_task.description = form.description.data
        new_task.due_date = form.due_date.data
        new_task.reminder = form.reminder.data
        new_task.CategoryID = form.category_id.data
        
        db.session.add(new_task)
        db.session.commit() 

        return redirect('/list')

    return render_template('create_book_form.html', form=form)