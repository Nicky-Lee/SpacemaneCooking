from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient,IGD_category
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN
from collections import defaultdict


def process_search_igd(request):
    igd_info = json.loads(request.data)
    igd_name = "%{}%".format(igd_info['igd_name'])
    igd = Ingredient.query.filter(Ingredient.igd_name.like(igd_name)).all()

    return igd


def process_search_igd_list(request):
    igd_info = json.loads(request.data)
    igd_name_list = igd_info['igd_name'].split(',')

    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()
    return igd_list

def process_Search_recipe(request):
    igd_info = json.loads(request.data)
    igd_name_list = igd_info['igd_name'].split(',')
    R_category = igd_info['R_category']
    if R_category is None:
        R_category = ['breakfast','lunch','dinner','dessert','else']
    # print('R_category',R_category)
    # print('igd_name_list',igd_name_list)
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()
    # print('igd_list_db',igd_list)
    R_id_dict= defaultdict(int)
    for igd in igd_list:
        # print("cur igd",igd.igd_name)
        R_list = igd.Recipe
        # print(R_list)
        for R in R_list:
            # print(R.R_name)
            if R.R_category in R_category:
                R_id_dict[R]+=1
    response_sorted = sorted(R_id_dict.items() ,key = lambda x:x[1],reverse=True)
    # print(response_sorted)
    response_sorted = [x for x,y in response_sorted]

    # print(response_sorted)
    # R = Recipe.query.join(test.Recipe)
    # print(R)
    # R_list = Recipe.query.filter(and_(Recipe.R_category == R_category,Recipe.Ingredient.igd_name.in_(igd_name_list))).all()
    # return R_list

    return response_sorted

def process_search_category_igd(request):
    igd_info = json.loads(request.data)
    igb_category = igd_info['igd_category']

    if igb_category is None:
        return None

    igd_list = IGD_category.query.filter(IGD_category.igd_category_name==igb_category).first().Ingredient
    print(igd_list)


    return igd_list
