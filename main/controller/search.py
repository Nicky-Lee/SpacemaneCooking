
from flask_restplus import Namespace, Resource, marshal
from flask import request, make_response, jsonify
import json
from ..server.search import *
from ..util.DTO import SearchDto
from ..util.decorator import token_optional, token_required

search_ns = SearchDto.search_ns

@search_ns.route("/user_recipe")
class user_recipe(Resource):
    # @search_ns.expect(SearchDto.search_recipe_model)

    @search_ns.response(0,"success",SearchDto.search_recipe_list_model_response)
    @token_required
    def post(self):

            return marshal(process_user_recipe(request),SearchDto.search_recipe_list_model_response),0


@search_ns.route("/initial_recommend")
class initial_recommend(Resource):
    # @search_ns.expect(SearchDto.search_recipe_model)
    @search_ns.response(0,"success",SearchDto.search_recipe_list_model_response)
    def post(self):

            return marshal(process_initial_recommend(),SearchDto.search_recipe_list_model_response),0

@search_ns.route("/select_recipe")
class select_recipe(Resource):
    @search_ns.expect(SearchDto.select_R_model_expect)
    @search_ns.response(0,"success",SearchDto.select_R_model_response)
    def post(self):
        # try:
            return marshal(process_select_recipe(request),SearchDto.select_R_model_response),0


@search_ns.route("/search_igd")
class Search_igd(Resource):
    @search_ns.expect(SearchDto.search_igd_model)
    @search_ns.response(0,"success",SearchDto.search_igd_list_model)
    def post(self):
        # try:
            return marshal(process_search_igd(request),SearchDto.search_igd_list_model),0
            # return process_search_igd(request)
        # except:
        #     return 'error request'

@search_ns.route("/search_igd_list")
class search_igd_list(Resource):
    @search_ns.expect(SearchDto.search_igd_model)
    @search_ns.response(0,"success",SearchDto.search_recipe_list_model_response)
    def post(self):
        # try:
        # process_search_igd(request)
            return marshal(process_search_igd_list(request),SearchDto.search_igd_list_model),0
        # except:
        #     return 'error request'

@search_ns.route("/search_recipe")
class Search_recipe(Resource):
    @search_ns.expect(SearchDto.search_recipe_model)
    @search_ns.response(0,"success",SearchDto.search_recipe_list_model_response)
    def post(self):
        # try:
        # process_search_igd(request)
            return marshal(process_Search_recipe(request),SearchDto.search_recipe_list_model_response),0
        # except:
        #     return 'error request'

@search_ns.route("/search_category_igd")
class search_category_igd(Resource):
    @search_ns.expect(SearchDto.search_category_igd_model)
    @search_ns.response(0,"success",SearchDto.search_category_igd_model_response)
    def post(self):
        # try:
        # process_search_igd(request)
            return marshal(process_search_category_igd(request),SearchDto.search_category_igd_model_response),0
        # except:
        #     return 'error request'

@search_ns.route("/get_all_igd_category")
class get_all_igd_category(Resource):
    # @search_ns.response(0,"success",SearchDto.get_all_igd_category_response)
    def post(self):
        # try:
        # process_search_igd(request)
            return marshal(process_get_all_igd_category(request),SearchDto.search_all_igd_category_response),0
        # except:
        #     return 'error request'

@search_ns.route("/get_all_R_tag")
class get_all_R_tag(Resource):
    # @search_ns.response(0,"success",SearchDto.get_all_igd_category_response)
    def post(self):
        # try:
        # process_search_igd(request)
            return process_get_all_R_tag(request)
        # except:
        #     return 'error request'

@search_ns.route("/igd_search_recipe")
class igd_search_recipe(Resource):
    @search_ns.expect(SearchDto.igd_search_recipe_model)
    @search_ns.response(0,"success",SearchDto.search_recipe_list_model_response)
    def post(self):
        # try:
        # process_search_igd(request)
        return marshal(process_igd_search_recipe(request), SearchDto.search_recipe_list_model_response), 0
        # except:
        #     return 'error request'