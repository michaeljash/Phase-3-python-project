import sqlite3

def connect_db():
    return sqlite3.connect('recipes.db')

def create_tables():
    conn = connect_db()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS recipe_ingredient (
        recipe_id INTEGER,
        ingredient_id INTEGER,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
    )
    ''')

    conn.commit()
    conn.close()


class Recipe:
    def _init_(self):
        self.CONN = sqlite3.connect("recipes.db")
        self.CURSOR = self.CONN.cursor()

class Users ):
    def __init__(self,name,description,id):
        self.name = name
        self.description = description
        self.id = id


if __name__ == "__main__":
    create_tables()
