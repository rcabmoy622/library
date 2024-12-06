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

        t1 = Book(title='Book 1', description='First book')
        t1.CategoryID = categories[0].id


        db.session.add_all([t1])
        db.session.commit()

if __name__ == '__main__':
    drop_tables()
    add_data_tables()