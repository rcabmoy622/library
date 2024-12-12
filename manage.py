from flask import  Flask
from library import app, db
from bbdd.db import *
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)
app.config['DEBUG'] = True

def create_tables():
    "Create relational database tables"
    with app.app_context():
        db.create_all()

def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA"
    with app.app_context():
        db.drop_all()

def add_data_tables():
    with app.app_context():
        db.create_all()

        "Adding categories"

        categories = [
            Category(name='Science'),
            Category(name='Technology'),
            Category(name='Education'),
            Category(name='Self-help'),
            Category(name='World History'),
            Category(name='Philosophy'),
            Category(name='Religion'),
            Category(name='Politics'),
            Category(name='Novel'),
            Category(name='Poetry'),
            Category(name='Theater'),
        ]

        db.session.add_all(categories)
        db.session.commit()

        "Adding states"

        states = [
            State(name='Available'),
            State(name='Checked Out'),
            State(name='Reserved'),
            State(name='Lost'),
            State(name='Damaged'),
            State(name='In Processing'),
            State(name='Archived'),
        ]
        
        db.session.add_all(states)
        db.session.commit()

        "Adding example books"

        books = [
            Book(title='Don Quijote de la Mancha',
                 description='A story about the adventures of a nobleman who becomes a knight-errant.', 
                 CategoryID=categories[8].id,
                   image="https://m.media-amazon.com/images/I/91CIwR3QU1L._UF1000,1000_QL80_.jpg"),
            Book(title='Romancero gitano', 
                 description='A collection of poems that explore Andalusian culture and gypsy themes.', 
                 CategoryID=categories[9].id,
                   image="https://m.media-amazon.com/images/I/81-8NaRIhnL._UF1000,1000_QL80_.jpg"),
            Book(title='The Metamorphosis', 
                 description='The surreal story of a man who wakes up transformed into a giant insect.', 
                 CategoryID=categories[8].id,
                   image="https://cdn.grupoelcorteingles.es/SGFM/dctm/MARKET/978/151/543/9781515431619_00_640x640.jpg?impolicy=Resize&width=1200&height=1200"),
            Book(title='In Search of Lost Time', 
                 description='A monumental work reflecting on time, memory, and society.', 
                 CategoryID=categories[8].id,
                   image="https://m.media-amazon.com/images/I/817hc-bhanL._UF1000,1000_QL80_.jpg"),
            Book(title='Hamlet', 
                 description='A tragedy about the Prince of Denmark and his quest for revenge.', 
                 CategoryID=categories[10].id,
                   image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX0cBq-pb5kBN33hhgkpJgBM5QfpSvwhRQmQ&s"),
            Book(title='Macbeth', 
                 description='A tragedy about ambition, power, and guilt in medieval Scotland.', 
                 CategoryID=categories[10].id,
                   image="https://m.media-amazon.com/images/I/81REk099uDL._AC_UF894,1000_QL80_.jpg"),
            Book(title='War and Peace', 
                 description='An epic novel about the Napoleonic wars and Russian society.', 
                 CategoryID=categories[8].id,
                   image="https://m.media-amazon.com/images/I/91teiIZ5vwL._UF1000,1000_QL80_.jpg"),
            Book(title='Anna Karenina', 
                 description='A tragic love story set in Russian aristocracy.', 
                 CategoryID=categories[8].id,
                   image="https://m.media-amazon.com/images/I/71z-a9gKZ4L._AC_UF1000,1000_QL80_.jpg"),
            Book(title='Mrs. Dalloway', 
                 description='A novel capturing a day in the life of Clarissa Dalloway in post-World War I England.', 
                 CategoryID=categories[8].id,
                   image="https://m.media-amazon.com/images/I/71+tcpXwNoL._AC_UF894,1000_QL80_.jpg"),
        ]

        db.session.add_all(books)
        db.session.commit()

        "Adding example authors"
        
        authors = [
            Author(name='Miguel de Cervantes', 
                   biography='Spanish writer, author of "Don Quijote de la Mancha".',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Cervantes_J%C3%A1uregui.jpg/1200px-Cervantes_J%C3%A1uregui.jpg"),
            Author(name='Federico García Lorca', 
                   biography='Spanish poet and playwright, known for "Romancero gitano".',
                   image="https://www.cervantesvirtual.com/images/portales/federico_garcia_lorca/graf/biografia/01-fotografia_de_federico_garcia_lorca_en_granada_en_1919_s.jpg"),
            Author(name='Franz Kafka', 
                   biography='Bohemian writer, known for "The Metamorphosis".',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Franz_Kafka%2C_1923.jpg/1200px-Franz_Kafka%2C_1923.jpg"),
            Author(name='Marcel Proust', 
                   biography='French writer, author of "In Search of Lost Time".',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Marcel_Proust_vers_1895.jpg/640px-Marcel_Proust_vers_1895.jpg"),
            Author(name='William Shakespeare', 
                   biography='English playwright and poet, author of "Hamlet" and "Macbeth".',
                   image="https://cdn.12min.com/books/books_background/60839_William_Shakespear.site_cover.jpg?1592262560"),
            Author(name='León Tolstói', 
                   biography='Russian novelist, author of "War and Peace" and "Anna Karenina".',
                   image="https://www.biografiasyvidas.com/biografia/t/fotos/tolstoi_leon.jpg"),
            Author(name='Virginia Woolf', 
                   biography='English modernist writer, known for "Mrs. Dalloway".',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Virginia_Woolf_1927.jpg/800px-Virginia_Woolf_1927.jpg"),
            Author(name='Paulo Coelho', 
                   biography='Brazilian writer, known for "The Alchemist".',
                   image="https://proassetspdlcom.cdnstatics2.com/usuaris/autores_fotos/fotos/1/original/157_1_1200x1200_coelho_FACEBOOK.jpg"),
            Author(name='Miguel de Unamuno', 
                   biography='Spanish writer and philosopher, author of "Abel Sánchez".',
                   image="https://imagessl.casadellibro.com/img/autores/w/unamuno_foto0.webp"),
        ]
        db.session.add_all(authors)
        db.session.commit()

        "Adding example book-author relations"

        book_author_relations = [
            BookAuthor(book_id=books[0].id, author_id=authors[0].id), # Don Quijote - Cervantes
            BookAuthor(book_id=books[1].id, author_id=authors[1].id), # Romancero gitano - Lorca
            BookAuthor(book_id=books[2].id, author_id=authors[2].id), # The Metamorphosis - Kafka
            BookAuthor(book_id=books[3].id, author_id=authors[3].id), # In Search of Lost Time - Proust
            BookAuthor(book_id=books[4].id, author_id=authors[4].id), # Hamlet - Shakespeare
            BookAuthor(book_id=books[5].id, author_id=authors[4].id), # Macbeth - Shakespeare
            BookAuthor(book_id=books[6].id, author_id=authors[5].id), # War and Peace - Tolstói
            BookAuthor(book_id=books[7].id, author_id=authors[5].id), # Anna Karenina - Tolstói
            BookAuthor(book_id=books[8].id, author_id=authors[6].id), # Mrs. Dalloway - Woolf
        ]
        db.session.add_all(book_author_relations)
        db.session.commit()


if __name__ == '__main__':
    drop_tables()
    create_tables()
    add_data_tables()