from cs50 import SQL

class Database:
    def __init__(self, sql):
        self.sql = sql

    def get_users(self):
        return self.sql.execute("SELECT * FROM users")

    def create_user(self, email, password_hash)
        self.sql.execute("INSERT INTO users (username, password_hash) VALUES(?, ?)", email, password_hash)