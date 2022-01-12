from flask_app.config.mysqlconnection import connectToMySQL as connect
from flask import flash
import datetime


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
    def get_recipes(cls, data = None):
        if data:
            query = '''SELECT id, name, description, under_30_min, instructions, date_recipe_made, user_id
            FROM recipes WHERE id = %(id)s;'''
            results = connect('recipes').query_db(query, data)
            if results[0] != None:
                return results[0]
            else: 
                return None
        else:
            query = '''SELECT id, name, description, under_30_min, instructions, date_recipe_made, user_id
            FROM recipes;'''
            results = connect('recipes').query_db(query)
        return results

    @classmethod
    def save_recipe(cls, data):
        query = '''INSERT INTO recipes (name, description, under_30_min, instructions, date_recipe_made, user_id)
        VALUES(%(name)s, %(description)s, %(under_30)s, %(instructions)s, %(date_recipe_made)s, %(user_id)s)'''
        connect('recipes').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = '''DELETE FROM recipes WHERE id = %(id)s;'''
        connect('recipes').query_db(query, data)

    
    
    
    
    
    
    
    @staticmethod
    def validate_recipe_input(data):
        year, month, day = data['date_recipe_made'].split('-')
        try:
            checkDate = datetime.date(int(year), int(month), int(day))
        except:
            checkDate = False
        is_valid = True
        validator = {
            'name' : {
                'check' : len(data['name']) >= 2,
                'message' : 'Name is too short!!'
            },
            'description' : {
                'check' : len(data['description']) > 2,
                'message' : 'Description is too short!!'
            },
            'under_30' : {
                'check' : data['under_30'] == '0' or data['under_30'] == '1',
                'message' : 'Invalid input for 30 minute question!!'
            },
            'instructions' : {
                'check' : len(data['instructions']) > 2,
                'message' : 'Instructions do not provide enough information!!'
            },
            'date_recipe_made' : {
                'check' : checkDate and datetime.date.today() >= checkDate,
                'message' : 'Invalid Date!'
            }            
        }
        for check in validator:
            if not validator[check]['check']:
                flash(validator[check]['message'])
                print(validator[check]['message'])
                is_valid = False
        return is_valid