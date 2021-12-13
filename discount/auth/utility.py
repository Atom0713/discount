import functools
import json
import os

from flask import Response, request, jsonify
from werkzeug.exceptions import abort
from http import HTTPStatus
import jwt

from discount import logger
from discount.common.constants import UserTypeConst, CustomResponse
from discount.discount_code.schemas import User, Merchant


def authentication(user_type: UserTypeConst):
    def authentication_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user_type not in UserTypeConst:
                abort(Response(json.dumps(CustomResponse.FAILED_TO_AUTHENTICATE), status=HTTPStatus.FORBIDDEN))


            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(' ')[1]

            if not token:
                return jsonify(CustomResponse.INVALID_TOKEN)
            try:
                data = jwt.decode(token, os.environ.get('SECRET_KEY', 'secret'), algorithms=["HS256"])
            except Exception as err:
                logger.exception(err)
                return jsonify(CustomResponse.INVALID_TOKEN)

            current_user = None
            if user_type == UserTypeConst.MERCHANT:
                current_user = Merchant.query.filter(Merchant.merchant_id == data['merchant_id']).first()
                kwargs['merchant'] = current_user

            elif user_type == UserTypeConst.USER:
                current_user = User.query.filter(User.user_id == data['user_id']).first()
                kwargs['user'] = current_user

            if not current_user:
                abort(Response(json.dumps(CustomResponse.FAILED_TO_AUTHENTICATE), status=HTTPStatus.FORBIDDEN))

            return func(*args, **kwargs)
        return wrapper

    return authentication_decorator
