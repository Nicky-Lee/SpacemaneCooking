from flask_restplus import Namespace, Resource, marshal
from flask import request, make_response, jsonify
import json
from ..server.user import *
from ..util.DTO import UserDto
from ..util.decorator import token_optional, token_required

user_ns = UserDto.user_ns
"""
1 data
2 status_code

200 ok
404 not fund
400 Bad request
401 User has no permissions.

当get请求时，需要使用request.args来获取数据

当post请求时，需要使用request.form来获取数据
"""
"""
1、POST /url 创建  
2、DELETE /url/xxx 删除 
3、PUT /url/xxx 更新
4、GET /url/xxx 查看
"""


# /auth/login
# @user_ns.route("/login")
# class UserLogin(Resource):
#
#     @user_ns.expect(UserDto.user_login_data_model)
#     @user_ns.response(200,'success',model=UserDto.user_model)
#     @user_ns.response(404, 'not find', model=UserDto.user_model)
#     def get(self):
#         user = process_login_v2(json.loads(request.data))
#         return marshal(user,UserDto.user_model),200

@user_ns.route("/userInfo")
class userInfo(Resource):
    @user_ns.expect(UserDto.user_model)
    @user_ns.response(200, "success", UserDto.user_model)
    def get(self):
        # if "address" in  request.args().keys():
        #     print(data)
        # try:

        return marshal(process_userInfo_v1(request),UserDto.user_model),200
    # except:
    #     return 'error request'

@user_ns.route("/login")
class UserLogin(Resource):
    @user_ns.expect(UserDto.user_login_data_model_expect)
    @user_ns.response(200, "success", UserDto.user_model)
    def post(self):

        try:
            return process_login_v1(json.loads(request.data))
        except:
            return 'error request'


@user_ns.route("/signup")
class UserSignup(Resource):
    @user_ns.expect(UserDto.user_UserSignup_data_model_expect)
    @user_ns.response(200, "success", UserDto.user_UserSignup_model_response)
    def post(self):
        # try:
            return process_signup_v1(json.loads(request.data))

        # except:
        #     return 'error request'


@user_ns.route("/forgetpassword")
class Forgetpassword(Resource):
    @user_ns.expect(UserDto.user_Forgetpassword_data_model_expect)
    @user_ns.response(200, "success", UserDto.user_Forgetpassword_model_response)
    # @token_required
    def post(self):
        # try:
            # print(json.loads(request.data))
            return process_forgetpassword_v1(request)
        # except:
        #     return 'error request'


@user_ns.route("/changepassword")
class ChangPassword(Resource):
    @user_ns.expect(UserDto.user_ChangPassword_data_model_expect)
    @user_ns.response(200, "success", UserDto.user_ChangPassword_model_response)
    @token_required
    def put(self):
        try:
            return process_changpassword_v1(request)
        except:
            return 'error request'

# @user_ns.route("/logot")
# class Logout(Resource):
#     @user_ns.expect(UserDto.user_ChangPassword_data_model_expect)
#     # @user_ns.response(200, "success", UserDto.user_ChangPassword_model_response)
#     @token_required
#     def post(self):
#         # try:
#             return process_logout_v1(request)
#         # except:
#         #     return 'error request'
