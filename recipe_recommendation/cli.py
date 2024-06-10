import models

def display_menu():
    print("1. Create User")
    print("2. Create Recipe")
    print("3. Create Ingredient")
    print("4. Delete User")
    print("5. Delete Recipe")
    print("6. Delete Ingredient")
    print("7. View All Users")
    print("8. View All Recipes")
    print("9. View All Ingredients")
    print("10. Find User by ID")
    print("11. Find Recipe by ID")
    print("12. Find Ingredient by ID")
    print("13. Exit")

def create_user():
    name = input("Enter user name: ")
    models.create_user(name)
    print("User created successfully.")

def create_recipe():
    title = input("Enter recipe title: ")
    description = input("Enter recipe description: ")
    user_id = int(input("Enter user ID: "))
    ingredient_ids = input("Enter ingredient IDs (comma separated): ")
    ingredient_ids = [int(id) for id in ingredient_ids.split(",")]
    models.create_recipe(title, description, user_id, ingredient_ids)
    print("Recipe created successfully.")

def create_ingredient():
    name = input("Enter ingredient name: ")
    models.create_ingredient(name)
    print("Ingredient created successfully.")

def delete_user():
    user_id = int(input("Enter user ID: "))
    models.delete_user(user_id)
    print("User deleted successfully.")

def delete_recipe():
    recipe_id = int(input("Enter recipe ID: "))
    models.delete_recipe(recipe_id)
    print("Recipe deleted successfully.")

def delete_ingredient():
    ingredient_id = int(input("Enter ingredient ID: "))
    models.delete_ingredient(ingredient_id)
    print("Ingredient deleted successfully.")

def view_all_users():
    users = models.get_all_users()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}")

def view_all_recipes():
    recipes = models.get_all_recipes()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Title: {recipe[1]}, Description: {recipe[2]}")

def view_all_ingredients():
    ingredients = models.get_all_ingredients()
    for ingredient in ingredients:
        print(f"ID: {ingredient[0]}, Name: {ingredient[1]}")

def find_user_by_id():
    user_id = int(input("Enter user ID: "))
    user = models.find_user_by_id(user_id)
    if user:
        print(f"ID: {user[0]}, Name: {user[1]}")
    else:
        print("User not found.")

def find_recipe_by_id():
    recipe_id = int(input("Enter recipe ID: "))
    recipe = models.find_recipe_by_id(recipe_id)
    if recipe:
        print(f"ID: {recipe[0]}, Title: {recipe[1]}, Description: {recipe[2]}")
    else:
        print("Recipe not found.")

def find_ingredient_by_id():
    ingredient_id = int(input("Enter ingredient ID: "))
    ingredient = models.find_ingredient_by_id(ingredient_id)
    if ingredient:
        print(f"ID: {ingredient[0]}, Name: {ingredient[1]}")
    else:
        print("Ingredient not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            create_recipe()
        elif choice == '3':
            create_ingredient()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            delete_ingredient()
        elif choice == '7':
            view_all_users()
        elif choice == '8':
            view_all_recipes()
        elif choice == '9':
            view_all_ingredients()
        elif choice == '10':
            find_user_by_id()
        elif choice == '11':
            find_recipe_by_id()
        elif choice == '12':
            find_ingredient_by_id()
        elif choice == '13':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
