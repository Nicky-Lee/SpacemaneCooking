
from flask_script import Manager
from main import app
from main.model.Recipe import *
from main.model.user import *
# from main.model.Recipe import IGD_category
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
def run():
    app.run()

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
    # db.drop_all()
    # db.create_all()
    # IGD_category_list = [IGD_category('egg'),
    #                      IGD_category("milk"),
    #                      IGD_category("meat")]
    # db.session.add_all(IGD_category_list)
    # db.session.commit()
    # manager.run()
    app.run()

