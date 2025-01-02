# Personal Library
This project is about a Flask Web to manage a Personal Library, including books, authors, categories, and states. The application provides a user-friendly interface to manage a book collection.  
Also, the web have user management (login and sign-up).  
The application will be available at http://localhost:5000/

# Features

- Book Management: Create, update, delete, and view books.
- Author Management: Add, update, delete, and view authors.
- User Authentication: Users can register, log in, and manage their profiles.

# Requirements

- Python 3.7 or higher
- Dependencies listed in requirements.txt

# Installation in Linux

1. Clone the repository:
  ```
  git clone https://github.com/rcabmoy622/library.git
  cd library
  ```

2. Create a virtual environment:
  ```
  python3 -m venv ./venv-library
  ```

3. Activate the virtual environment:
  ```
  source ./venv-library/bin/activate
  ```

4. Install dependencies:
  ```
  pip install -r requirements.txt
  ```

5. Set up the database:
> [!IMPORTANT]
> It is very important to execute 'manage.py' to create the tables of our database and add data to it.
  ```
  python3 manage.py
  ```

6. Run the application:
  ```
   flask --app ./library.py run --host=0.0.0.0
  ```