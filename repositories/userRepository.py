from models.user import User
from extensions import db 

class userRepository:
    @staticmethod
    def create(username, email, password):
        user = User(user= username, email=email, password= password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    