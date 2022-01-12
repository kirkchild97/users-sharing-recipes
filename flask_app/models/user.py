from flask_app.config.mysqlconnection import connectToMySQL as connect
import re
from flask_app.models.recipe import Recipe
from flask import flash

class User:
    def __init__(self, data: dict) -> None:
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_user(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email, password)
        VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);'''
        connect('recipes').query_db(query, data)

    @classmethod
    def get_user_login(cls, data):
        query = '''SELECT id, email, password FROM users
        WHERE email = %(email)s;'''
        results = connect('recipes').query_db(query, data)
        if results != None:
            return results[0]
        else:
            return False

    @classmethod
    def login_user(cls, data):
        query = '''SELECT id, first_name, last_name, email FROM users WHERE id = %(id)s;'''
        results = connect('recipes').query_db(query, data)
        user_data = {
            'user_info' : results[0]
        }
        user_data['recipes'] = Recipe.get_recipes()
        return user_data









    @staticmethod
    def validate_user_data(data:dict) -> bool:
        check_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        validate = {
            'first_name' : {
                'check' : len(data['first_name']) > 2,
                'message' : 'First Name Does not meet length requirement of 2'
            },
            'last_name' : {
                'check' : len(data['last_name']) > 2,
                'message' : 'Last Name Does not meet length requirement of 2'
            },
            'email' : {
                'check' : check_email.match(data['email']),
                'message' : 'Not a valid email'
            },
            'password' : {
                'check' : data['password'] == data['con_password'],
                'message' : 'Passwords do not match'
            }
        }
        for check in validate:
            if not validate[check]['check']:
                flash(validate[check]['message'])
                is_valid = False
        return is_valid
    
    @staticmethod
    def check_for_email(data:dict):
        query = '''SELECT email FROM users WHERE email = %(email)s'''
        results = connect('recipes').query_db(query, data)
        print('Results: ', results)
        check = False
        if 'email' in results:
            check = results['email'] == data['email']
            if  check:
                flash('Email already used for another account!')
        return check