from flask_restplus import Namespace, Resource,marshal
from ..util.DTO import RecipeDto
from ..server.recipe import *
from flask import request, make_response, jsonify
import json

from ..util.decorator import token_required

Recipe_ns = RecipeDto.Recipe_ns
# /auth/login

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

    def get(self):
        try:
            return process_select_igd_v1(json.loads(request.data))
        except:
            return 'error request'


@Recipe_ns.route("/uploadImage")
class  UploadImage_v1(Resource):

    @Recipe_ns.response(200,"success",RecipeDto.image_model_response)
    def post(self):
        # try:
            return marshal(process_uploadImage(request),RecipeDto.image_model_response),200
        # except:
        #     return 'error request'

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