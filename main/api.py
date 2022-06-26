from flask import Blueprint
from flask_restplus import Api, Resource
from .util.DTO import UserDto, RecipeDto
from .controller.user import user_ns
from .controller.recipe import Recipe_ns
# from .util.DTO import RecipeDto
# from .util.DTO import UserDto
blueprint = Blueprint("api", __name__)
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

api = Api(
    blueprint,
    title="SpacemanCooking api",
    version='1.0',
    description='the introduction of api using in backend.',
    # authorizations={
    #     "ApiKey":{
    #         "type":"ApiKey",
    #         'name':'token_cookie_check',
    #         "in":"header"
    #     }
    # },
    # secrets="ApiKey"
)
# Recipe_ns = RecipeDto.Recipe_ns
# user_ns = UserDto.user_ns
api.add_namespace(user_ns, "/User")
api.add_namespace( Recipe_ns, "/Recipe")
