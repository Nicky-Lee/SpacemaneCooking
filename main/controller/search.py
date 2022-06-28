from flask_restplus import Namespace, Resource, marshal
from flask import request, make_response, jsonify
import json
from ..server.search import *
from ..util.DTO import SearchDto
from ..util.decorator import token_optional, token_required

search_ns = SearchDto.search_ns


@search_ns.route("/search_igd")
class Search_igd(Resource):
    @search_ns.expect(SearchDto.search_igd_model)
    @search_ns.response(200,"success",SearchDto.search_igd_list_model)
    def get(self):
        # try:
            return marshal(process_search_igd(request),SearchDto.search_igd_list_model),200
            # return process_search_igd(request)
        # except:
        #     return 'error request'

@search_ns.route("/search_igd_list")
class search_igd_list(Resource):
    @search_ns.expect(SearchDto.search_igd_model)
    @search_ns.response(200,"success",SearchDto.search_recipe_list_model_response)
    def get(self):
        # try:
        # process_search_igd(request)
            return marshal(process_search_igd(request),SearchDto.search_igd_list_model),200
        # except:
        #     return 'error request'

@search_ns.route("/search_recipe")
class Search_recipe(Resource):
    @search_ns.expect(SearchDto.search_recipe_model)
    @search_ns.response(200,"success",SearchDto.search_recipe_list_model_response)
    def get(self):
        # try:
        # process_search_igd(request)
            return marshal(process_search_igd(request),SearchDto.search_recipe_list_model_response),200
        # except:
        #     return 'error request'
