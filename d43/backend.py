import sqlite3

db_url = "books.db"

def connect():
    db = sqlite3.connect(db_url)
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS book
        (id INTEGER PRIMARY KEY,
         title TEXT,
         author TEXT,
         year INTEGER,
         isbn INTEGER); 
        """)
    db.commit()
    db.close()

def insert(title, author, year, isbn):
    db = sqlite3.connect(db_url)
    c = db.cursor()

    c.execute("INSERT INTO book VALUES (NULL,?, ?, ?, ?);", (title, author, year, isbn))

    db.commit()
    db.close()

def view():
    db = sqlite3.connect(db_url)
    c = db.cursor()

    c.execute("SELECT * FROM book;")
    rows = c.fetchall()
    db.commit()
    db.close()
    return rows

def search(title='', author='', year='', isbn=''):
    db = sqlite3.connect(db_url)
    c = db.cursor()

    c.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?;", (title, author, year, isbn))
    rows = c.fetchall()
    db.commit()
    db.close()
    return rows
    
def delete(id):
    db = sqlite3.connect(db_url)
    c = db.cursor()

    c.execute("DELETE FROM book WHERE id=?;", (id,))

    db.commit()
    db.close()

def update(id, title, author, year, isbn):
    db = sqlite3.connect(db_url)
    c = db.cursor()

    c.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?;", (title, author, year, isbn, id))

    db.commit()
    db.close()

    
connect()