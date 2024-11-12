import sqlite3


class Database:
    def __init__(self, db_name='user_db'):
        self.Connection = sqlite3.connect(db_name)
        self.cursor = self.Connection.cursor
        self.creat_table()
        
    def create_table(self):
        self.cursor.execute("""
              CREATE TABLE IF NOT EXISTS users(
                  id INTEGER PRIMARY KEY AUTOINCTRMENT
                  name VARCHAR 40 NOT NULL
                  email TEXT UNIQUE NOT NULL
                  age INT
              )                
    """)
        
       
    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (user.name, 
        user.email, user.age))
        
        self.Connection.commit()
        
    def get_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone()
    
    def close(self):
        self.Connection.close()