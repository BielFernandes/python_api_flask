from flask import Blueprint
from mongoengine import *

defaultRoute = '/users'

user_bp = Blueprint('users', __name__)

@user_bp.route('/register')
def user_register():
    connect(host="mongodb://127.0.0.1:27017/my_db")

    class User(Document):
        email = StringField(required=True)
        first_name = StringField(max_length=50)
        last_name = StringField(max_length=50)

        def say_name(self):
            return f'hello my name is {self.first_name}'


    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley')

    print(ross.say_name())
    print(ross)

@user_bp.route(f'{defaultRoute}/profile')
def user_profile():
    return '<p> USER PROFILE </p>'
