from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient, IGD_category
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN
from collections import defaultdict
from ..model.Recipe import Recipe

def process_user_recipe(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)
    R = Recipe.query.filter(Recipe.user_id == user.id).all()
    code =400
    if R:
        code=200
    return R,code


def process_select_recipe(request):
    R_name = json.loads(request.data)['R_name']
    R = Recipe.query.filter(Recipe.R_name == R_name).first()
    code =400
    if R:
        R.click = R.click + 1
        db.session.add(R)
        db.session.commit()
        code = 200

    return R,code


def process_search_fuzzy_igd_Recipe(request):
    igd_info = json.loads(request.data)
    igd_name = "%{}%".format(igd_info['igd_name'])
    dict = {"igd":None,"Recipe":None}
    igd = Ingredient.query.filter(Ingredient.igd_name.like(igd_name)).all()
    R = Recipe.query.filter(Recipe.R_name.like(igd_name)).first()
    code = 400
    if igd:
        code = 200
        igd_list = []
        for i in igd:
            igd_list.append(i.igd_name)
        dict['igd'] = igd_list

    if R:
        code = 200
        # R_list = []
        # for i in R:
        # R_list.append(R.R_name)
        dict['Recipe'] = R.R_name

    resp = make_response(jsonify(dict))
    resp.status_code = code

    return resp

def process_R_category_search_recipe(request):
    code = 400
    R_category = json.loads(request.data)['R_category']
    R_list = Recipe.query.filter(Recipe.R_category == R_category).all()

    if R_list:
        code = 200
    return R_list,code

def process_search_igd_list(request):
    igd_info = json.loads(request.data)
    igd_name_list = igd_info['igd_name'].split(',')

    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()
    code = 400
    if igd_list:
        code = 200
    return igd_list,code


def process_Search_recipe(request):
    code = 400
    igd_info = json.loads(request.data)
    igd_name_list = igd_info['igd_name'].split(',')
    R_category = igd_info['R_category'].split(',')
    # if R_category is None:
    #     R_category = ['breakfast', 'lunch', 'dinner', 'dessert', 'else']
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()
    R_id_dict = defaultdict(int)
    for igd in igd_list:
        R_list = igd.Recipe
        for R in R_list:
            for R_cat in R_category:
                if R_cat in R.R_category:
                    R_id_dict[R] += 1
                    break
    response_sorted = sorted(R_id_dict.items(), key=lambda x: x[1], reverse=True)
    response_sorted = [x for x, y in response_sorted]

    if R_id_dict:
        code = 200
    return response_sorted,code


def process_igd_search_recipe(request):
    igd_info = json.loads(request.data)
    igd_name_list = igd_info['igd_name'].split(',')
    code = 400
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()

    R_id_dict = defaultdict(int)
    for igd in igd_list:
        R_list = igd.Recipe
        for R in R_list:
            R_id_dict[R] += 1
    response_sorted = sorted(R_id_dict.items(), key=lambda x: x[1], reverse=True)
    response_sorted = [x for x, y in response_sorted]

    if R_id_dict:
        code = 200

    return response_sorted,code

def process_initial_recommend():
    code = 400
    R_list = Recipe.query.filter(Recipe.R_name != '').all()
    R_list_dict = defaultdict(int)
    for R in R_list:
        Recipe_click = R.click
        R_list_dict[R] += Recipe_click
    response_sorted = sorted(R_list_dict.items(), key=lambda x: x[1], reverse=True)
    response_sorted = [x for x, y in response_sorted]

    if R_list:
        code = 200
    return response_sorted,code


def process_search_category_igd(request):
    igd_info = json.loads(request.data)
    igb_category = igd_info['igd_category']
    code = 400
    if igb_category is None:
        return None

    igd_list = IGD_category.query.filter(IGD_category.igd_category_name == igb_category).first()
    # print(igd_list)
    # print(igd_list)
    if igd_list:
        igd_list= igd_list.Ingredient
    # print(igd_list)
        code = 200

    return igd_list,code


def process_get_all_igd_category(request):
    # print(IGD_category.query(IGD_category.igd_category_name).all())
    all_igd_category = IGD_category.query.filter(IGD_category.igd_category_name != '').all()
    code = 400
    if all_igd_category:
        code = 200
    return all_igd_category,code


def process_get_all_R_tag(request):
    # print(IGD_category.query(IGD_category.igd_category_name).all())
    all_R_tag_list = []
    all_R_tag = Recipe.query.filter(Recipe.R_category != '').all()
    for tag in all_R_tag:
        for each_tag in tag.R_category.split(','):
            if each_tag != '' and each_tag not in all_R_tag_list:
                all_R_tag_list.append(each_tag)
            # print(each_tag)
    response_data = {"all_R_tag": all_R_tag_list}

    status_code = 200

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return resp
