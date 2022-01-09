from flask_app.config.mysqlconnection import connectToMySQL as connect

class Recipe:
    def __init__(self, data: dict) -> None:
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_recipes(cls):
        query = '''SELECT id, name, description, under_30, instructions, date_recipe_made, user_id
        FROM recipes;'''
        results = connect('recipes').query_db(query)
        return results

    @classmethod
    def save_recipe(cls, data):
        query = '''INSERT INTO recipes (name, description, under_30, instructions, date_recipe_made, user_id)
        VALUES(%(name)s, %(description)s, %(under_30)s, %(instructions)s, %(date_recipe_made)s, %(user_id)s)'''
        connect('recipes').query_db(query, data)