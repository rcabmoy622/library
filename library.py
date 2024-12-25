from flask import Flask, abort, render_template, request, redirect, flash, g
import config
from bbdd.db import Book, Category, Author, State, BookAuthor, User, db
from forms.library_forms import BookForm, AuthorForm, SignupForm, LoginForm, ProfileForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.init_app(app)
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        g.profile_picture_url = current_user.profilePicture or 'https://static.vecteezy.com/system/resources/previews/042/156/821/non_2x/user-3d-graphic-illustration-free-png.png'
        g.username = current_user.name

@app.route('/not_found/')
def not_found():
    return render_template('not_found.html'), 404 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/faqs/')
def faqs():
    return render_template('faqs.html')

@app.route('/bookshelf/')
@login_required
def list_books():
    query = request.args.get('search_performed', '')

    if query:
        books = Book.query.filter(Book.title.ilike(f'%{query}%')).all()
    else:
        books = Book.query.all()
    return render_template('bookshelf.html', books=books, search_performed=query)

@app.route('/authors/')
@login_required
def list_authors():
    query = request.args.get('search_performed', '')

    if query:
        authors = Author.query.filter(Author.name.ilike(f'%{query}%')).all()
    else:
        authors = Author.query.all()
    return render_template('authors.html', authors=authors, search_performed=query)

@app.route('/book/<int:id>/')
@login_required
def view_book_details(id):
    book = Book.query.filter_by(id=id).first()

    if book:
        return render_template('book_details.html', book=book)
    else:
        abort(404)

@app.route('/author/<int:id>/')
@login_required
def view_author_details(id):
    author = Author.query.filter_by(id=id).first()

    if author:
        return render_template('author_details.html', author=author)
    else:
        abort(404)

@app.route('/book/create/', methods=["get","post"])
@login_required
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

    return render_template('create_book.html', form=form)

@app.route('/author/create/', methods=["get","post"])
@login_required
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

    return render_template('create_author.html', form=form)

@app.route('/book/<int:id>/update/', methods=["get","post"])
@login_required
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

        # Delete existing book-author relationships
        BookAuthor.query.filter_by(book_id=book.id).delete()

        # Create selected book-author relationships
        selected_authors = form.author.data
        for author_id in selected_authors:
            book_author = BookAuthor(book_id=book.id, author_id=author_id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/bookshelf/')
    
    current_authors = [author.author_id for author in book.book_authors]
    form.author.data = current_authors
    form.category_id.data = book.CategoryID
    form.state_id.data = book.StateID

    return render_template('update_book.html', book=book, form=form)

@app.route('/author/<int:id>/update/', methods=["get","post"])
@login_required
def update_author(id):
    author = Author.query.filter_by(id=id).first()

    form = AuthorForm(request.form, obj=author)
    form.book.choices = [(book.id, book.title) for book in Book.query.all()]

    if form.validate() and request.method == "POST":
        author.name = form.name.data
        author.biography = form.biography.data
        author.image = form.image.data
 
        # Delete existing author-book relationships
        BookAuthor.query.filter_by(author_id=author.id).delete() 

        # Create Selected Author-Book Relationships
        selected_books = form.book.data 
        for book_id in selected_books:
            book_author = BookAuthor(book_id=book_id, author_id=author.id)
            db.session.add(book_author)

        db.session.commit()

        return redirect('/authors/')
    
    current_books = [book_author.book_id for book_author in author.book_authors]
    form.book.data = current_books

    return render_template('update_author.html', author=author, form=form)

@app.route('/book/<int:id>/delete/')
@login_required
def delete_book(id):
    book = Book.query.filter_by(id=id).first()
    BookAuthor.query.filter_by(book_id=book.id).delete()
    db.session.delete(book)
    db.session.commit()
    return redirect('/bookshelf')

@app.route('/author/<int:id>/delete/')
@login_required
def delete_author(id):
    author = Author.query.filter_by(id=id).first()
    BookAuthor.query.filter_by(author_id=author.id).delete()
    db.session.delete(author)
    db.session.commit()
    return redirect('/authors')

@app.route('/search/', methods=['get'])
@login_required
def search():
    query = request.args.get('search_performed')
    book_results = Book.query.filter(Book.title.ilike(f'%{query}%')).all()
    author_results = Author.query.filter(Author.name.ilike(f'%{query}%')).all()

    return render_template('search_results.html', book_results=book_results, author_results=author_results, query=query)

@app.route('/signup/', methods=["get","post"])
def signup():   
    form = SignupForm(request.form)

    if form.validate() and request.method == "POST":
        # If this returns a user, then the email exists in database
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email address already exists', 'danger')
            return redirect('/signup/')

        new_user = User()
        new_user.email=form.email.data
        new_user.name=form.name.data
        new_user.password=generate_password_hash(form.password.data, method='pbkdf2:sha256')

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect('/login/')
    
    return render_template('signup.html', form=form)

@app.route('/login/', methods=["get","post"])
def login():
    form = LoginForm(request.form)
    next_url = request.args.get('next', '/profile/')
    
    if form.validate() and request.method == "POST":
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
        
        user = User.query.filter_by(email=email).first()

        # Check if the user exists
        if not user or not check_password_hash(user.password, password):
            flash('Incorrect email or password. Try again.', 'danger')
            return redirect(f'/login/?next={next_url}')

        login_user(user, remember=remember)
        flash('Welcome back!', 'success')

        return redirect(next_url or '/profile/')
    
    return render_template('login.html', form=form)

@app.route('/profile/', methods=["get", "post"])
@login_required
def profile():
    user = current_user
    form = ProfileForm(request.form, obj=user)

    total_books = Book.query.count()

    total_authors = Author.query.count()

    category_with_most_books = db.session.query(
        Category.name, db.func.count(Book.id).label('book_count')
        ).join(Book, Book.CategoryID == Category.id).group_by(Category.id).order_by(db.desc('book_count')).first()
    
    author_with_most_books = db.session.query(
        Author.name, db.func.count(Book.id).label('book_count')
        ).join(Book.authors).group_by(Author.id).order_by(db.desc('book_count')).first()


    if form.validate() and request.method == "POST":
        # Check if the email exists and is not of the current user
        existing_user = User.query.filter(User.email == form.email.data, User.id != user.id).first()
        if existing_user:
            flash('Email address already exists.', 'danger')
            return redirect('/profile/')

        user.name = form.name.data
        user.email = form.email.data

        if form.profilePicture.data:
            user.profilePicture = form.profilePicture.data
        else:
            user.profilePicture = 'https://static.vecteezy.com/system/resources/previews/042/156/821/non_2x/user-3d-graphic-illustration-free-png.png'
        
        if form.password.data:
            user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        
        return redirect('/profile/')
    
    return render_template('profile.html', 
                           form=form, 
                           name=user.name, 
                           email=user.email, 
                           total_books=total_books, 
                           total_authors=total_authors, 
                           category_with_most_books=category_with_most_books,
                           author_with_most_books=author_with_most_books
                           )

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/delete_account/', methods=["post"])
@login_required
def delete_account():
    db.session.delete(current_user)
    db.session.commit()

    logout_user()
    return redirect('/')