from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient,IGD_category
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN


def image_information(request):
    data = request.Tests
    print(data)

    return data


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
             "image_id": None,
             "R_igd_list": R_info['R_igd_list'],
             "message": "fail to upload！"}
    R_igd_list = R_info["R_igd_list"].split(',')
    R_igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(R_igd_list))

    Rec = Recipe.query.filter_by(R_name=R_info['R_name']).first()
    if not Rec:
        for key in R_info.keys():
            if key in R_dic.keys():
                R_dic[key] = R_info[key]

        Rec = Recipe(R_name=R_dic['R_name'],
                     R_category=R_dic["R_category"],
                     user_id=R_dic['user_id'],
                     R_description=R_dic['R_description'],
                     R_calorie=R_dic['R_calorie'],
                     R_img_url=R_dic['image_id'])
        for igd in R_igd_list:
            igd.recipe.append(Rec)
            db.session.add(igd)

        db.session.add(Rec)
        db.session.commit()

        R_dic['message'] = f"{R_info['R_name']} upload successfully!!"
    else:
        R_dic['message'] = f"{R_info['R_name']} already exist!!"
        status_code = 400

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
            # print(igd_ca.igd_category)
            # print(i)
            # i+=1
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
