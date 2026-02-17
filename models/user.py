from extensions import db
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        password_encode = password.encode('utf-8')[:72]
        self.password = pbkdf2_sha256.hash(password_encode)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.user,
            'email': self.email
        }