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
                 description='A story about the adventures of a nobleman who becomes a knight-errant, embarking on a quest to revive chivalry. His journey is filled with absurd and humorous episodes, offering deep insights into the human condition.',
                 CategoryID=categories[8].id,
                 StateID=states[0].id,
                 image="https://m.media-amazon.com/images/I/91CIwR3QU1L._UF1000,1000_QL80_.jpg"),
            Book(title='Romancero gitano', 
                 description='A collection of poems that explore Andalusian culture, gypsy themes, and the tragic, passionate lives of its characters. Lorca blends folklore, mysticism, and the harsh reality of life in the Spanish countryside.',
                 CategoryID=categories[9].id,
                 StateID=states[6].id,
                 image="https://m.media-amazon.com/images/I/81-8NaRIhnL._UF1000,1000_QL80_.jpg"),
            Book(title='The Metamorphosis', 
                 description='The surreal story of Gregor Samsa, a man who wakes up one morning to find himself transformed into a giant insect. His alienation from his family and society explores themes of isolation, identity, and the absurdity of existence.',
                 CategoryID=categories[8].id,
                 StateID=states[5].id,
                 image="https://cdn.grupoelcorteingles.es/SGFM/dctm/MARKET/978/151/543/9781515431619_00_640x640.jpg?impolicy=Resize&width=1200&height=1200"),
            Book(title='In Search of Lost Time', 
                 description='A monumental, seven-volume work that delves deeply into themes of time, memory, and society. The novel reflects on the fluid nature of time and the complexities of human relationships.',
                 CategoryID=categories[8].id,
                 StateID=states[2].id,
                 image="https://m.media-amazon.com/images/I/817hc-bhanL._UF1000,1000_QL80_.jpg"),
            Book(title='Hamlet', 
                 description='A tragedy that explores the themes of revenge, madness, betrayal, and mortality. The story follows Prince Hamlet’s quest to avenge his father’s murder by his uncle, now the king of Denmark.',
                 CategoryID=categories[10].id,
                 StateID=states[0].id,
                 image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX0cBq-pb5kBN33hhgkpJgBM5QfpSvwhRQmQ&s"),
            Book(title='Macbeth', 
                 description='A tragedy about unchecked ambition and the consequences of power. Macbeth, spurred by his wife and prophecies from three witches, embarks on a murderous path that leads to his downfall.',
                 CategoryID=categories[10].id,
                 StateID=states[2].id,
                 image="https://m.media-amazon.com/images/I/81REk099uDL._AC_UF894,1000_QL80_.jpg"),
            Book(title='War and Peace', 
                 description='An epic novel set during the Napoleonic wars that explores the intersection of personal lives and historical events. The novel weaves together themes of love, duty, and the effects of war on individuals and society.',
                 CategoryID=categories[8].id,
                 StateID=states[3].id,
                 image="https://m.media-amazon.com/images/I/91teiIZ5vwL._UF1000,1000_QL80_.jpg"),
            Book(title='Anna Karenina', 
                 description='A tragic love story set within the Russian aristocracy. Anna’s passionate affair with Count Vronsky leads to a moral crisis that destroys her family and her place in society, reflecting the tensions of 19th-century Russian society.',
                 CategoryID=categories[8].id,
                 StateID=states[1].id,
                 image="https://m.media-amazon.com/images/I/71z-a9gKZ4L._AC_UF1000,1000_QL80_.jpg"),
            Book(title='Mrs. Dalloway', 
                 description='A novel set in post-World War I England, focusing on Clarissa Dalloway as she prepares for a party. The book delves into her reflections on life, love, and the passage of time, as well as her interactions with other characters.',
                 CategoryID=categories[8].id,
                 StateID=states[4].id,
                 image="https://m.media-amazon.com/images/I/71+tcpXwNoL._AC_UF894,1000_QL80_.jpg"),
        ]

        db.session.add_all(books)
        db.session.commit()

        "Adding example authors"
        
        authors = [
            Author(name='Miguel de Cervantes', 
                   biography='Miguel de Cervantes Saavedra was a Spanish writer, poet, and playwright, best known for "Don Quijote de la Mancha". He is considered one of the most important figures in Spanish literature and one of the greatest writers in Western literature.',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Cervantes_J%C3%A1uregui.jpg/1200px-Cervantes_J%C3%A1uregui.jpg"),
            Author(name='Federico García Lorca', 
                   biography='Federico García Lorca was a Spanish poet, playwright, and theatre director, born in Andalusia. He is considered one of the most important Spanish poets of the 20th century. His works often explore themes of love, death, and Spanish identity.',
                   image="https://www.cervantesvirtual.com/images/portales/federico_garcia_lorca/graf/biografia/01-fotografia_de_federico_garcia_lorca_en_granada_en_1919_s.jpg"),
            Author(name='Franz Kafka', 
                   biography='Franz Kafka was a German-speaking Bohemian writer, widely regarded as one of the most influential writers of the 20th century. His works often explore themes of alienation, bureaucracy, and the absurdity of life.',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Franz_Kafka%2C_1923.jpg/1200px-Franz_Kafka%2C_1923.jpg"),
            Author(name='Marcel Proust', 
                   biography='Marcel Proust was a French writer, best known for his seven-volume series "In Search of Lost Time". His works focus on the involuntary memory and are regarded as one of the greatest literary achievements of the 20th century.',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Marcel_Proust_vers_1895.jpg/640px-Marcel_Proust_vers_1895.jpg"),
            Author(name='William Shakespeare', 
                   biography='William Shakespeare was an English playwright, poet, and actor, widely regarded as one of the greatest writers in the English language. His plays, such as "Hamlet" and "Macbeth", explore themes of ambition, power, love, and tragedy.',
                   image="https://cdn.12min.com/books/books_background/60839_William_Shakespear.site_cover.jpg?1592262560"),
            Author(name='León Tolstói', 
                   biography='Leo Tolstoy was a Russian writer, philosopher, and social reformer. His novels, including "War and Peace" and "Anna Karenina", explore complex themes of morality, free will, and the search for meaning in life.',
                   image="https://www.biografiasyvidas.com/biografia/t/fotos/tolstoi_leon.jpg"),
            Author(name='Virginia Woolf', 
                   biography='Virginia Woolf was an English writer, one of the most important modernist authors of the 20th century. Her works, such as "Mrs. Dalloway" and "To the Lighthouse", explore themes of time, identity, and the inner lives of women.',
                   image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Virginia_Woolf_1927.jpg/800px-Virginia_Woolf_1927.jpg"),
            Author(name='Paulo Coelho', 
                   biography='Paulo Coelho is a Brazilian author best known for "The Alchemist", a novel that has been translated into numerous languages and is one of the best-selling books in history. His works often explore spirituality, personal growth, and the pursuit of dreams.',
                   image="https://proassetspdlcom.cdnstatics2.com/usuaris/autores_fotos/fotos/1/original/157_1_1200x1200_coelho_FACEBOOK.jpg"),
            Author(name='Miguel de Unamuno', 
                   biography='Miguel de Unamuno was a Spanish writer, philosopher, and university professor. His works, including "Abel Sánchez", explore existential themes and the human struggle for meaning, blending philosophical inquiry with literary creativity.',
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