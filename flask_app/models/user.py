from flask_app.config.mysqlconnection import connectToMySQL as connect

class User:
    def __init__(self, data: dict) -> None:
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']