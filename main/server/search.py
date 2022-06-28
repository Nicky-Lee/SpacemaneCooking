from ..model.user import User, UserInf
from ..model.Recipe import Recipe, Ingredient,IGD_category
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
import json
from ..util.token import TOKEN



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

