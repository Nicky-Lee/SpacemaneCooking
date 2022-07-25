from flask_script import Manager
from main import app
from main.model.Recipe import *
from main.model.user import *
# from main.model.Recipe import IGD_category
from main.api import blueprint
import pandas as pd
import random
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
    # IGD_category_list = [IGD_category('Tubers'), IGD_category("Melon and Fruits"), IGD_category("Stems"),
    #                      IGD_category("Aquatic product"),
    #                      IGD_category("Eggs"), IGD_category("Chicken"), IGD_category("Beef"), IGD_category("Pork"),
    #                      IGD_category("Mutton"), IGD_category("Flour and rice product"), IGD_category("Mushrooms"),
    #                      IGD_category("Onion garlic"),
    #                      IGD_category("Bean products"), IGD_category("Beans"), IGD_category("Dairy product"),
    #                      IGD_category("Condiments"),
    #                      IGD_category("Other types"), IGD_category("Cereal")]
    # db.session.add_all(IGD_category_list)
    # IGB_list = []
    # igb_df = pd.read_excel(r'E:\we_content\WeChat Files\wxid_7316523165111\FileStorage\File\2022-07\main(1)\main\SpacemaneCooking\database_message.xlsx',sheet_name='Sheet2')
    # """
    # Ingredient(igd_name=igd_dic['igd_name'],
    #                      igd_category=igd_dic["igd_category"],
    #                      igd_opponent=igd_dic['igd_opponent'],
    #                      igd_calorie=igd_dic['igd_calorie'],
    #                      image_id=igd_dic['image_id'])
    #                      """
    # for index in igb_df.index:
    #     igd_name = igb_df.iloc[index, 0]
    #     igd_category = igb_df.iloc[index, 1]
    #     igd_opponent = igb_df.iloc[index, 2]
    #     igd_calorie = int(igb_df.iloc[index, 3])
    #     tmp = Ingredient(igd_name=igd_name,
    #                      igd_category=igd_category,
    #                      igd_opponent=igd_opponent,
    #                      igd_calorie=igd_calorie)
    #     db.session.add(tmp)
    #     db.session.commit()
    #
    #     igd_ca = IGD_category.query.filter(IGD_category.igd_category_name == igd_category).first()
    #     igd_ca.Ingredient.append(tmp)
    #     db.session.add(igd_ca)
    #     db.session.commit()
    #
    # R_list = pd.read_excel(r'E:\we_content\WeChat Files\wxid_7316523165111\FileStorage\File\2022-07\main(1)\main\SpacemaneCooking\database_message.xlsx', sheet_name='Sheet1')
    # """
    # Rec = Recipe(R_name=R_dic['R_name'],
    #                  R_category=R_dic["R_category"],
    #                  user_id=R_dic['user_id'],
    #                  R_description=R_dic['R_description'],
    #                  R_calorie=R_dic['R_calorie'],
    #                  R_img_url=R_dic['image_id'],
    #                  Ingredient_content = R_info['igd_list'],
    #                  click = random.randint(1,100))
    #                      """
    # for index in R_list.index:
    #     R_name = R_list.iloc[index, 0]
    #     R_description = R_list.iloc[index, 1]
    #     R_category = R_list.iloc[index, 2]
    #     igd_calorie = int(R_list.iloc[index, 3])
    #     Ingredient_content= R_list.iloc[index, 4]
    #     Rec = Recipe(R_name=R_name,
    #                  R_category=R_category,
    #                  user_id=1,
    #                  R_description=R_description,
    #                  R_calorie=igd_calorie,
    #                  image_id=index+1,
    #                  Ingredient_content=Ingredient_content,
    #                  click=random.randint(1, 100))
    #     db.session.add(Rec)
    #     db.session.commit()
    #
    #     igd_list = Ingredient_content.split(',')
    #     igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_list)).all()
    #     for igd in igd_list:
    #         igd.Recipe.append(Rec)
    #         db.session.add(igd)
    #
    #     db.session.add(Rec)
    #     db.session.commit()

    app.run()
