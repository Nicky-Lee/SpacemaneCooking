from functools import wraps
from flask import request, make_response, jsonify
from .token import TOKEN

def token_required(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        token = request.headers.get("token")
        if not token:
            resp = make_response(jsonify({"error": "token is missing"}))
            resp.status_code = 401
            return resp
        user = TOKEN.validate_token(token)

        if not user:
            resp = make_response(jsonify({"error": "invalid token"}))
            resp.status_code = 401
            return resp
        # print(user.id)

        return f(*args, **kwargs)
    return decorate


def token_optional(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        token = request.headers.get("token")
        user =None
        if token:
            user = TOKEN.validate_token(token)

        return f(*args, **kwargs)

    return decorate

