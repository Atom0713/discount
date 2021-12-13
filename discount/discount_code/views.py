import json

from flask import Blueprint, request, jsonify, Response
from werkzeug.exceptions import abort
from http import HTTPStatus

from discount.auth.utility import authentication
from discount.common.constants import UserTypeConst, HTTPMethodsConst, CustomResponse
from discount.common.utility import get_json_or_abort
from discount.discount_code.controller import DiscountCodeController
from discount.discount_code.schemas import Merchant, User

bp = Blueprint('discount_code', __name__, url_prefix='/discount_code')


@bp.route('/merchant/manage/', methods=[HTTPMethodsConst.GET, HTTPMethodsConst.POST])
@authentication(UserTypeConst.MERCHANT)
def discount(merchant: Merchant):
    if request.method == HTTPMethodsConst.POST:
        return jsonify(DiscountCodeController.create_discount_codes_by_merchant(merchant, get_json_or_abort()))

    elif request.method == HTTPMethodsConst.GET:
        return jsonify(DiscountCodeController.retrieve_all_discount_codes_by_merchant(merchant))

    else:
        abort(Response(json.dumps(CustomResponse.FAILED), status=HTTPStatus.METHOD_NOT_ALLOWED))


@bp.route('/user/<int:merchant_id>/', methods=[HTTPMethodsConst.GET])
@authentication(UserTypeConst.USER)
def get_discount(user: User, merchant_id: int):
    if request.method == HTTPMethodsConst.GET:
        return jsonify(DiscountCodeController.retrieve_single_discount_code_by_merchant(user, merchant_id))
    else:
        abort(Response(json.dumps(CustomResponse.FAILED), status=HTTPStatus.METHOD_NOT_ALLOWED))
