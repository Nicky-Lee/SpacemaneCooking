# from flask_script import Manager
from main import app
from main.model.Recipe import *
from main.model.user import *
# from main.model.Recipe import IGD_category
from main.api import blueprint
import pandas as pd
import random
import sys

app = app
app.register_blueprint(blueprint)

#
# manager = Manager(app)


# #
# @app.route('user/<number>')
# def user_register(number):
#     pass
#
# @manager.command
# def run():
#     app.run()
#
#
# @manager.command
# def create_all():
#     db.create_all()
#
#
# @manager.command
# def drop_all():
#     db.drop_all()
#
#
# @manager.command
# def db_init():
#     app.db_init()


# from recipe import recipe_blue
# from user import user_blue

# app.register_blueprint(recipe_blue)
# app.register_blueprint(user_blue)


if __name__ == '__main__':

    if len(sys.argv) >= 2:
        mark = sys.argv[1]
    else:
        mark = 'run'

    if mark == 'init':
        db.drop_all()
        db.create_all()
        print('create IGD_category')
        IGD_category_list = [IGD_category('vegetables'), IGD_category("meat"), IGD_category("mushrooms"),
                             IGD_category("beans and bean products"), IGD_category("aquatic products"),
                             IGD_category("eggs"), IGD_category("fruits"), IGD_category("dairy products"),
                             IGD_category("cereal"), IGD_category("condiments"), IGD_category("other types")]
        db.session.add_all(IGD_category_list)
        db.session.commit()
        IGB_list = []
        igb_df = pd.read_excel('database_igd.xlsx')
        """
        Ingredient(igd_name=igd_dic['igd_name'],
                             igd_category=igd_dic["igd_category"],
                             igd_opponent=igd_dic['igd_opponent'],
                             igd_calorie=igd_dic['igd_calorie'],
                             image_id=igd_dic['image_id'])
        """
        for index in igb_df.index:
            igd_category = igb_df.iloc[index, 0]
            igd_name = igb_df.iloc[index, 1].lower()

            igd_calorie = int(igb_df.iloc[index, 2])
            igd_opponent = igb_df.iloc[index, 3]
            tmp = Ingredient(igd_name=igd_name,
                             igd_category=igd_category,
                             # igd_opponent=igd_opponent,
                             igd_calorie=igd_calorie)
            db.session.add(tmp)
            db.session.commit()
            # print(igd_category,igd_name)
            igd_ca = IGD_category.query.filter(IGD_category.igd_category_name == igd_category).first()
            igd_ca.Ingredient.append(tmp)
            db.session.add(igd_ca)
            db.session.commit()
        print('upload Recipe')

        R_list = pd.read_excel(r'database_recipe.xlsx')
        """
        Rec = Recipe(R_name=R_dic['R_name'],
                         R_category=R_dic["R_category"],
                         user_id=R_dic['user_id'],
                         R_description=R_dic['R_description'],
                         R_calorie=R_dic['R_calorie'],
                         image_url=R_dic['image_url'],
                         Ingredient_content = R_info['igd_list'],
                         click = random.randint(1,100))
        """


        def Calorie_counting(igd_g_list):
            igd_g_list = igd_g_list.split(';')
            c_res = 0
            Ingredient_conten = ''

            for tmp in igd_g_list:
                try:
                    igd, num = tmp.split(',')
                    igd = Ingredient.query.filter(Ingredient.igd_name == igd.lower()).first()
                    if igd:
                        Ingredient_conten += igd.igd_name + ','
                        c_res += igd.igd_calorie * int(num) * 0.01
                except:
                    print(tmp)

            return int(c_res), Ingredient_conten[:-1]


        for index in R_list.index:
            R_name = R_list.iloc[index, 1]
            Ingredient_g_content = R_list.iloc[index, 2].lower()
            R_description = R_list.iloc[index, 3]
            R_category = R_list.iloc[index, 4]
            image_url = R_list.iloc[index, 5]



            R_calorie, Ingredient_content = Calorie_counting(Ingredient_g_content)

            igd_list_search = Ingredient_content.split(',')
            igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_list_search)).all()

            Rec = Recipe(R_name=R_name,
                         R_category=R_category,
                         user_id=random.randint(1, 6),
                         R_description=R_description,
                         R_calorie=R_calorie,
                         image_url=image_url,
                         Ingredient_g_content=Ingredient_g_content,
                         Ingredient_content=Ingredient_content,
                         click=random.randint(1, 100))
            db.session.add(Rec)
            db.session.commit()

            for igd in igd_list:
                igd.Recipe.append(Rec)
                db.session.add(igd)

            db.session.add(Rec)
            db.session.commit()
        igd_oppoist_list = pd.read_excel(r'database_opposit.xlsx')
        print('upload igd_oppoist ')

        for index in igd_oppoist_list.index:
            igd_igd = igd_oppoist_list.iloc[index, 0].lower()
            igd_igd1 = sorted(igd_igd.split(';'))
            igd_igd2 =','.join(igd_igd1)
            reason = igd_oppoist_list.iloc[index, 1]


            igd_op = IGD_opposite.query.filter(IGD_opposite.igd_igd == igd_igd2).all()

            if igd_op:
                continue

            igd_op_tmp  = IGD_opposite(igd_igd=igd_igd2,
                         reason=reason)
            db.session.add(igd_op_tmp)
            db.session.commit()

        user = [("Nikcy",'z5229785',"871511711@qq.com"),
                ("Nikcya",'z5229785',"871511711a@qq.com"),
                ("Nikcyb",'z5229785',"871511711b@qq.com"),
                ("Nikcyaa",'z5229785',"871511711aa@qq.com"),
                ("Nikcybb",'z5229785',"871511711bb@qq.com"),
                ("Nikcybbc",'z5229785',"871511711bbc@qq.com")]
        for username,key,email in user:
            new_user = User(username=username, password=key, email=email)
            db.session.add(new_user)
            db.session.commit()

        Search_lack = [("garlic,tofu", 5),
                ("garlic,salt,tofu", 3),
                ("garlic,salt", 2),
                ("pepper,salt", 3) ]
        for searc, time  in Search_lack:
            new_Search = Search(search=searc, time=time)
            db.session.add(new_Search)
            db.session.commit()
    else:
        pass


    app.run()
