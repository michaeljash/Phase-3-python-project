import sqlite3
from db import connect_db

def create_user(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

def find_user_by_id(user_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def create_recipe(title, description, user_id, ingredient_ids):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO recipes (title, description, user_id) VALUES (?, ?, ?)', (title, description, user_id))
    recipe_id = c.lastrowid
    for ingredient_id in ingredient_ids:
        c.execute('INSERT INTO recipe_ingredient (recipe_id, ingredient_id) VALUES (?, ?)', (recipe_id, ingredient_id))
    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    c.execute('DELETE FROM recipe_ingredient WHERE recipe_id = ?', (recipe_id,))
    conn.commit()
    conn.close()

def get_all_recipes():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM recipes')
    recipes = c.fetchall()
    conn.close()
    return recipes

def find_recipe_by_id(recipe_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    recipe = c.fetchone()
    conn.close()
    return recipe

def create_ingredient(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO ingredients (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def delete_ingredient(ingredient_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
    conn.commit()
    conn.close()

def get_all_ingredients():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM ingredients')
    ingredients = c.fetchall()
    conn.close()
    return ingredients

def find_ingredient_by_id(ingredient_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
    ingredient = c.fetchone()
    conn.close()
    return ingredient
