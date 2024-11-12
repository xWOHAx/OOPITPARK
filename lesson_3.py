from database import database

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    
class UserService:
    def __init__(self, db_name = 'user_db'):
        self.db = database(db_name)

    def add_user(self, user):
        if self.find_user_by_email(user.email):
            print('Почта уже испоьзуется')
            return
        self.db.add_user(user)
        print('Успешно')
        
    def find_user_by_email(self, email):
        user_data = self.db.get_user(email)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print('Ошибка')
            
    def delete_user_by_email(self, email):
        self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
        self.Connection.commit()
            
    def close(self):
        self.db.close()