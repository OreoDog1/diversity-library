from flask_mysqldb import MySQL

class Database:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_users(self):
        return self.execute("SELECT * FROM users")

    def create_user(self, email, password_hash):
        return self.execute("INSERT INTO users (email, password_hash) VALUES(%s, %s)", (email, password_hash))

    def find_user(email):
        try:
            return self.execute("SELECT * FROM users WHERE email = ?", (email))[0]
        except:
            return None

    def execute(self, query, queryVars=()):
        # Check if there are variables to plug in
        if len(queryVars) == 0:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, queryVars)
        self.cursor.connection.commit()
        return self.cursor.fetchall()
