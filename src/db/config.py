from mongoengine import *
import json
import datetime

connect('testemongod')

class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField()
    bio = StringField(max_length=100)
    admin = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "bio": self.bio,
            "admin": self.admin,
            "date_created": self.date_created
        }

        return json.dumps(user_dict)
    
    meta = {
        'indexes': ['username', 'email'],
        'ordering': ['-date_created'],
    }