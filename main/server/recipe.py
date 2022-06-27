from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN


# def image_information(request):
#     data = db.session.query(Ingredient.name,Ingredient.days)
#
#     return data


def process_UploadRecipe(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)
    R_info = json.loads(request.data)

    status_code = 200
    R_dic = {"R_name": R_info['R_name'],
             "user_id": user.id,
             "R_description": None,
             "R_category": None,
             "R_calorie": 0,
             "R_img_url": None,
             "message": "fail to upload！"}

    Rec = Recipe.query.filter_by(R_name=R_info['R_name']).first()
    print(1)
    if not Rec:
        for key in R_info.keys():
            if key in R_dic.keys():
                R_dic[key] = R_info[key]

        print(2)
        Rec = Recipe(R_name=R_dic['R_name'],
                     R_category=R_dic["R_category"],
                     user_id=R_dic['user_id'],
                     R_description=R_dic['R_description'],
                     R_calorie=R_dic['R_calorie'],
                     R_img_url=R_dic['R_img_url'])
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
    igd_dic = {"igd_name": None,
               "igd_category": None,
               "igd_opponent": None,
               "igb_description": None,
               "igd_calorie": 0
               }

    igd_dic["igd_img_url"] = image_information(request)
    # print(image_information(request))
    igd = Ingredient.query.filter(Ingredient.igd_name == igd_info['igd_name']).first()
    if not igd:
        for key in igd_info.keys():
            if key in igd_dic.keys():
                igd_dic[key] = igd_info[key]

        igd = Ingredient(igd_name=igd_dic['igd_name'],
                         igd_category=igd_dic["igd_category"],
                         igd_opponent=igd_dic['igd_opponent'],
                         igb_description=igd_dic['igb_description'],
                         igd_calorie=igd_dic['igd_calorie'],
                         igd_img_url=igd_dic['igd_img_url'])
        db.session.add(igd)
        db.session.commit()
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
