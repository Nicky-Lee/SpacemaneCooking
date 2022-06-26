
from flask_script import Manager
from main import app
from main.model.Recipe import *
from main.model.user import *
from main.api import blueprint


app = app
app.register_blueprint(blueprint)


#
manager = Manager(app)
# #
# @app.route('user/<number>')
# def user_register(number):
#     pass

@manager.command
def create_all():
    db.create_all()

@manager.command
def drop_all():
    db.drop_all()


@manager.command
def db_init():
    app.db_init()

# from recipe import recipe_blue
# from user import user_blue

# app.register_blueprint(recipe_blue)
# app.register_blueprint(user_blue)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(port=5000)


