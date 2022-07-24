from flask_restplus import Namespace, Resource
from ..util.DTO import RecipeDto
from ..server.recipe import *
from flask import request, make_response, jsonify
import json

from ..util.decorator import token_required

Recipe_ns = RecipeDto.Recipe_ns
# /auth/login

# @Recipe_ns.route("/Count_calories")
# class Count_calories(Resource):
#     # @Recipe_ns.expect(RecipeDto.Recipe_model_upload)
#     @token_required
#     def post(self):
#         # try:
#         #     print('1221')
#             return process_Count_calories(request)

@Recipe_ns.route("/image_upload")
class image_upload(Resource):
    # @Recipe_ns.expect(RecipeDto.Recipe_model_upload)
    @token_required
    def post(self):
        # try:
        #     print('1221')
            return process_image_upload(request)


@Recipe_ns.route("/image_get")
class image_get(Resource):
    # @Recipe_ns.expect(RecipeDto.Recipe_model_upload)
    # @token_required
    def post(self):
        # try:
        return process_image_get(request)


@Recipe_ns.route("/uploadRecipe")
class UploadRecipe(Resource):
    @Recipe_ns.expect(RecipeDto.Recipe_model_upload)
    @token_required
    def post(self):
        # try:
            return process_UploadRecipe(request)
        # except:
        #     return 'error request'


# @Recipe_ns.route("/changeRecipe")
# class ChangeRecipe(Resource):
#
#     def put(self):
#         try:
#             return process_login_v1(json.loads(request.data))
#         except:
#             return 'error request'


@Recipe_ns.route("/upload_igd_managerment")
class Upload_igd(Resource):
    @Recipe_ns.expect(RecipeDto.Ingredient_model_upload)
    @token_required
    def post(self):
        # try:
            return process_upload_igd(request)
        # except:
        #     return 'error request'


@Recipe_ns.route("/SearchRecipe")
class  Select_igd_v1(Resource):

    def post(self):
        try:
            return process_select_igd_v1(json.loads(request.data))
        except:
            return 'error request'

# # 限制条件
# # 1，原材料
# # 2，菜谱种类
# # 3，
# @Recipe_ns.route("/SearchRecipe")
# class  Select_recipe_v1(Resource):
#
#     def get(self):
#         try:
#             return process_Select_recipe_v1(json.loads(request.data))
#         except:
#             return 'error request'