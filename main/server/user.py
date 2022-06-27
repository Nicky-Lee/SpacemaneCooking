from ..model.user import User, UserInf
from flask import make_response, jsonify
from .. import *
from sqlalchemy import and_, or_
from ..util.token import TOKEN
import json


# get
def process_userInfo_v1(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)


    return user



# get
def process_login_v1(user_info):
    response_data = {"username": user_info['username'], "email": None, "id": None, "message": "success", "token": None}
    status_code = 200
    user = User.query.filter_by(username=user_info["username"]).first()
    if user is None:
        response_data['message'] = 'failed,user is None'
        status_code = 400
        print('zheli')

    elif user.password != user_info['password']:
        response_data['message'] = 'failed, password error'
        status_code = 400

    if status_code == 200:
        token = TOKEN.generate_token(user.id)
        response_data['token'] = token
        response_data['email'] = user.email
        response_data['id'] = user.id

    resp = make_response(jsonify(response_data))
    print(resp)
    resp.status_code = status_code

    return resp


def process_login_v2(user_info):
    response_data = {"username": user_info['username'], "message": "success"}
    status_code = 200

    user = User.query.filter_by(username=user_info["username"]).first()
    if user is None:
        response_data['message'] = 'failed,user is None'
        status_code = 400

    if user.password != user_info['password']:
        response_data['message'] = 'failed, password error'
        status_code = 400
    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return user


def valid_regist(username, email):
    user = User.query.filter(or_(User.username == username, User.email == email)).first()
    if user:
        return False
    else:
        return True


def password_invalid(password):
    longth = len(password)
    if longth > 15 or longth < 8:
        return True
    elif ' ' in password:
        return True
    else:
        return False


# post
def process_signup_v1(user_info):
    response_data = {"username": user_info['username'], "message": "fail to sign in！"}
    status_code = 200
    if user_info['password1'] != user_info['password2']:
        response_data['message'] = 'The passwords are different！'

    elif password_invalid(user_info['password1']):
        response_data['message'] = 'The password is invalid！'
        status_code = 411

    elif valid_regist(user_info['username'], user_info['email']):
        user = User(username=user_info['username'], password=user_info['password1'],
                    email=user_info['email'])
        db.session.add(user)
        db.session.commit()

        response_data['message'] = "register successfully！"

    else:
        response_data['message'] = 'The username or email address is already registered！'

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code

    return resp


# get
def process_forgetpassword_v1(request):
    # token = request.headers.get("token")
    # user = TOKEN.validate_token(token)
    user_info = json.loads(request.data)
    response_data = {"username":user_info['username'], "message": 'Information error'}
    status_code = 200

    user = User.query.filter(User.username == user_info['username']).first()
    if user is None:
        response_data['message'] = f'username not exist!'
        status_code = 400

    if user.email == user_info['email']:
        response_data['message'] = f'success, password is {user.password}'
        print(1)

    else:
        response_data['message'] = 'failed, email error!'
        status_code = 400
    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return resp


# put
def process_changpassword_v1(request):
    token = request.headers.get("token")
    user = TOKEN.validate_token(token)

    user_info = json.loads(request.data)
    response_data = {"username": None, "new_password":None,"message": 'Information error'}
    status_code = 200

    # user = User.query.filter_by(username=user_id).first()
    response_data['username'] = user.username
    if user is None:
        response_data['message'] = 'failed,user is None'
        status_code = 400
    elif user_info['old_password'] == user_info['new_password']:
        response_data['message'] = 'failed, The passwords are same！'
        status_code = 400


    elif user.password == user_info['old_password']:
        if password_invalid(user_info['new_password']):
            response_data['message'] = f'failed, new password is Invalid '
        else:
            user.password = user_info['new_password']
            db.session.add(user)
            db.session.commit()
            response_data['message'] = f'success'
            response_data['new_password'] = user_info['new_password']
            status_code = 200

    else:
        response_data['message'] = 'failed, password error'
        status_code = 400

    resp = make_response(jsonify(response_data))
    resp.status_code = status_code
    return resp
