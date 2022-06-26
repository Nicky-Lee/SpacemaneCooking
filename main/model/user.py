from main import db
from .. import db


# from flask import Blueprint

# user_manage = Blueprint('user_manage', __name__)


# 定义ORM
# 和菜谱表是1对多：1人对多个表
# 定义ORM
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    online = db.Column(db.Boolean, nullable=True)
    upload_Recipe = db.relationship("Recipe", backref="User")

    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class UserInf(db.Model):
    __tablename__ = 'userinf'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(80), nullable=True)
    ingredient_dislike = db.Column(db.String(120), nullable=True)
    Recipe_preference = db.Column(db.String(120), nullable=True)
    ingredient_preference = db.Column(db.String(120), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    hobby = db.Column(db.String(80), nullable=True)
    occupation = db.Column(db.String(80), nullable=True)
    nation = db.Column(db.String(80), nullable=True)

    def __init__(self, age=None, ingredient_dislike=None, Recipe_preference=None,
                 ingredient_preference=None, gender=None, hobby=None,
                 occupation=None, nation=None):
        self.age = age
        self.ingredient_dislike = ingredient_dislike
        self.Recipe_preference = Recipe_preference
        self.ingredient_preference = ingredient_preference
        self.gender = gender
        self.hobby = hobby
        self.occupation = occupation
        self.nation = nation
