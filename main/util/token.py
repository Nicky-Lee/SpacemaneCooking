from itsdangerous import SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as JWTSerializer, JSONWebSignatureSerializer
from time import time
from ..model.user import User


class UserToken:
    def __init__(self, secret_key, expires_in):
        self.secret_key = secret_key
        self.expires_in = expires_in
        self.serializer = JSONWebSignatureSerializer(secret_key)

    def generate_token(self, userid):
        self.serializer = JWTSerializer(
            secret_key=key,
            expires_in=self.expires_in
        )

        payload = {
            "id": userid,
            "time": time()
        }

        token = self.serializer.dumps(payload)

        return token.decode()

    def validate_token(self, token):
        try:
            payload = self.serializer.loads(token.encode())
        except (SignatureExpired, BadSignature):
            return None
        user = User.query.filter_by(id=payload['id']).first()
        # user = db.select([census]).where(census.columns.sex == 'F')User.query(id==payload['id']).first


        return user


key = "&&&$$$***"
EXPIRE_IN = 6000
TOKEN = UserToken(key, EXPIRE_IN)
