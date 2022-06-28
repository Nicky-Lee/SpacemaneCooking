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
    igd_list = Ingredient.query.filter(Ingredient.igd_name.in_(igd_name_list)).all()
    R_id_list = defaultdict(int)
    for igd in igd_list:
        R_list = igd.Recipe
        for R in R_list:
            if R.R_category == R_category:
                R_id_list[R]+=1

    print(R_id_list)
    # R = Recipe.query.join(test.Recipe)
    # print(R)
    # R_list = Recipe.query.filter(and_(Recipe.R_category == R_category,Recipe.Ingredient.igd_name.in_(igd_name_list))).all()
    # return R_list

    return 0