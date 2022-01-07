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