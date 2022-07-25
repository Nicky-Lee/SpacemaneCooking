from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient, IGD_category, Image
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN
import random
from .. import IMAGE_PATH

"""R_category_num={

1:breakfast
2:lunch
3:dinner
4:dessert
5:else
}"""


# def process_Count_calories(request):
#     data = json.loads(request.data)['image_get']
#     igd_num_dict = {}
#     igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_num_dict.keys())).all()
#     resp = make_response(jsonify(response_data))
#     resp.status_code = 200
#     return

def Calorie_counting(igd_g_list):
    igd_g_list = igd_g_list.split(';')
    c_res = 0
    Ingredient_conten = ''
    for tmp in igd_g_list:
        igd, num = tmp.split(',')
        igd = Ingredient.query.filter(Ingredient.igd_name == igd).first()
        if igd:
            Ingredient_conten += igd.igd_name + ','
            c_res += igd.igd_calorie * int(num) * 0.01

    return int(c_res), Ingredient_conten


def process_change_Recipe(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)
    R_info = json.loads(request.data)

    status_code = 200
    R_dic = {"R_name": R_info['R_name'],
             "user_id": user.id,
             "R_description": R_info['R_description'],
             "R_category": R_info['R_category'],
             "R_calorie": 0,
             "image_id": R_info['image_id'],
             "igd_list": R_info['igd_list'],
             "message": "fail to upload！"}
    igd_list = R_info["igd_list"].split(',')
    # print(igd_list)
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_list)).all()
    # print(igd_list)

    Rec = Recipe.query.filter_by(id=R_info['R_id']).first()
    if igd_list == []:
        status_code = 400
        R_dic['message'] = f"Ingredient not exist!!"
    elif Rec:
        if Rec.user_id == user.id:
            # if R_dic['R_category'] not in ['breakfast','lunch','dinner','dessert']:
            #     R_dic['R_category'] = 'else'
            db.session.delete(Rec)
            db.session.commit()

            click = Rec.click
            igd_g_list = R_dic['igd_list']

            R_calorie, Ingredient_content = Calorie_counting(igd_g_list)
            new_Rec = Recipe(R_name=R_dic['R_name'],
                             R_category=R_dic["R_category"],
                             user_id=user.id,
                             R_description=R_dic['R_description'],
                             R_calorie=R_calorie,
                             image_id=R_dic['image_id'],
                             Ingredient_g_content=R_info['igd_list'],
                             Ingredient_content=Ingredient_content,
                             click=click)

            # print(R_dic)
            for igd in igd_list:
                igd.Recipe.append(new_Rec)
                db.session.add(igd)

            db.session.add(new_Rec)
            db.session.commit()

            R_dic['message'] = f"{R_info['R_name']} upload successfully!!"
        else:
            R_dic['message'] = f"this user did not upload id  {R_info['R_id']} Recipe !!"
            status_code = 400
    else:
        R_dic['message'] = f"this user did not upload id  {R_info['R_id']} Recipe !!"
        status_code = 400

    # Rec = Recipe.query.filter_by(R_name=R_info['R_name']).first()
    # print(Rec.Ingredient)

    resp = make_response(jsonify(R_dic))
    resp.status_code = status_code

    return resp


def process_image_upload(request):
    # print(1)
    data = request.files['file']
    # print(data)

    try:
        image_data = data.read()

        image = Image(image_data)
        db.session.add(image)
        db.session.commit()
        # print(image)
        response_data = {'image_id': image.id}

        f = open(f"{IMAGE_PATH}{image.id}.png",'wb')
        f.write(image_data)
        f.close()


        code = 200
    except:
        response_data = {}
        code = 400

    resp = make_response(jsonify(response_data))
    resp.status_code = code
    return resp


def process_image_get(request):
    image_id = json.loads(request.data)['image_get']
    image = Image.query.filter(Image.id == image_id).first()
    # response_data = {'image': image.image}
    # print(image.image)
    if image:
        resp = make_response(image.image)
        code = 200
    else:
        resp = make_response(None)
        code = 400
    resp.status_code = code

    return resp


def process_UploadRecipe(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)
    R_info = json.loads(request.data)

    status_code = 200
    R_dic = {"R_name": R_info['R_name'],
             "user_id": user.id,
             "R_description": R_info['R_description'],
             "R_category": R_info['R_category'],
             "R_calorie": 0,
             "image_id": R_info['image_id'],
             "igd_list": R_info['igd_list'],
             "message": "fail to upload！"}
    igd_list = R_info["igd_list"].split(',')
    # print(igd_list)
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_list)).all()
    # print(igd_list)

    Rec = Recipe.query.filter_by(R_name=R_info['R_name']).first()
    if igd_list == []:
        R_dic['message'] = f"Ingredient not exist!!"
        status_code = 400
    elif Rec is None and igd_list != []:

        igd_g_list = R_info['igd_list']

        R_calorie, Ingredient_content = Calorie_counting(igd_g_list)
        Rec = Recipe(R_name=R_dic['R_name'],
                     R_category=R_dic["R_category"],
                     user_id=R_dic['user_id'],
                     R_description=R_dic['R_description'],
                     R_calorie=R_calorie,
                     image_id=R_dic['image_id'],
                     Ingredient_g_content=R_info['igd_list'],
                     Ingredient_content=Ingredient_content,
                     click=random.randint(1, 100))
        for igd in igd_list:
            igd.Recipe.append(Rec)
            db.session.add(igd)

        db.session.add(Rec)
        db.session.commit()
        R_dic['R_calorie']=R_calorie

        R_dic['message'] = f"{R_info['R_name']} upload successfully!!"
    else:
        R_dic['message'] = f"{R_info['R_name']} already exist!!"
        status_code = 400

    # Rec = Recipe.query.filter_by(R_name=R_info['R_name']).first()
    # print(Rec.Ingredient)

    resp = make_response(jsonify(R_dic))
    resp.status_code = status_code

    return resp


# post just for managerment!!!!
def process_upload_igd(request):
    igd_info = json.loads(request.data)

    response_data = {"igd_name": igd_info['igd_name'], "message": "fail to upload！"}
    status_code = 200
    igd_dic = {
        "igd_name": igd_info['igd_name'],
        "igd_category": igd_info['igd_category'],
        "igd_opponent": igd_info['igd_opponent'],
        "igd_calorie": igd_info['igd_calorie'],
        "image_id": igd_info["image_id"]
    }

    # igd_dic["igd_img_url"] = image_information(request)
    igd = Ingredient.query.filter(Ingredient.igd_name == igd_info['igd_name']).first()
    igd_category_list = igd_dic['igd_category'].split(',')
    igd_category = IGD_category.query.filter(IGD_category.igd_category_name.in_(igd_category_list)).all()
    if not igd and igd_category:
        igd = Ingredient(igd_name=igd_dic['igd_name'],
                         igd_category=igd_dic["igd_category"],
                         igd_opponent=igd_dic['igd_opponent'],
                         igd_calorie=igd_dic['igd_calorie'],
                         image_id=igd_dic['image_id'])
        db.session.add(igd)
        db.session.commit()
        for igd_ca in igd_category:
            igd_ca.Ingredient.append(igd)
            db.session.add(igd_ca)

        db.session.commit()
        # test = IGD_category.query.filter(IGD_category.igd_category_name=="egg").first()
        # for i in test.Ingredient:
        #     print(type(i))
        #     print(i.igd_name)
        # test2 = Ingredient.query.filter(test).all()
        # print(test2)
        response_data['message'] = f"{igd_info['igd_name']} upload successfully!!"
    else:
        response_data['message'] = f"{igd_info['igd_name']} already exist!!"
        status_code = 400

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code

    return resp


# get
def process_select_igd_v1(igd_info):
    response_data = {"igd_name": igd_info['igd_name'], "message": "success"}
    status_code = 200

    igd = Ingredient.query.filter_by(username=igd_info["igd_name"]).first()
    if igd is None:
        response_data['message'] = 'failed,Ingredient is not exist'
        status_code = 400
    else:
        response_data['message'] = 'failed,Ingredient is not exist'

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return resp
