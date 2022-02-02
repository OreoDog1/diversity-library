from cs50 import SQL

class Database:
    def __init__(self, sql):
        self.sql = sql

    def get_users(self):
        return self.sql.execute("SELECT * FROM users")

    def create_user(self, email, password_hash)
        self.sql.execute("INSERT INTO users (email, password_hash) VALUES(?, ?)", email, password_hash)

    def find_user(email):
        try:
            return self.sql.execute("SELECT * FROM users WHERE email = ?", email)[0]
        except:
            return None