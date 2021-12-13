from datetime import datetime, timedelta
import random
from typing import List

from discount import logger
from discount.common.constants import CustomResponse
from discount.discount_code.schemas import Merchant, User, DiscountSetting
from discount.discount_code.sql import DiscountCodeSQL


class DiscountCodeController:

    @staticmethod
    def generate_discount_code(count: int, discount_settings: DiscountSetting) -> List[str]:
        discount_codes: List[str] = []
        for i in range(count):
            discount_code: str = ""
            for x in range(discount_settings.code_length):
                discount_code += random.choice(discount_settings.code_origin)
            discount_codes.append(discount_code)

        return discount_codes

    @staticmethod
    def create_discount_codes_by_merchant(merchant: Merchant, json_data: dict):
        try:
            discount_settings: DiscountSetting = DiscountCodeSQL.get_discount_code_settings(merchant.merchant_id)
            discount_code_config: dict = json_data['discount_code_config']

            discount_codes = DiscountCodeController.generate_discount_code(
                discount_code_config['count'], discount_settings)

            discount_config: list = [
                {
                    'code': code,
                    'value': discount_code_config['value'],
                    'discount_type_id': discount_code_config['discount_type_id'],
                    'merchant_id': merchant.merchant_id,

                }
                for code in discount_codes]

            _ = DiscountCodeSQL.save_discount_codes(discount_config)
            return CustomResponse.ok_with_kwargs()
        except Exception as err:
            logger.exception(err)
            return CustomResponse.FAILED

    @staticmethod
    def retrieve_all_discount_codes_by_merchant(merchant: Merchant):
        return CustomResponse.ok_with_kwargs(
            all_active_discount_codes=DiscountCodeSQL.get_all_active_discount_codes_by_merchant(merchant.merchant_id))

    @staticmethod
    def prepare_merchant_message(user: User, merchant_id: int):
        message = {'user_id': user.user_id, 'merchant_id': merchant_id}
        return message

    @staticmethod
    def retrieve_single_discount_code_by_merchant(user: User, merchant_id: int):
        discount_code = DiscountCodeSQL.get_and_reserve_discount_code(user.user_id, merchant_id)
        if not discount_code:
            return CustomResponse.failed_with_kwargs(message='There are no available discount codes.')

        # _ = send_message_to_sqs(SQSTopics.SHARE_USER_INFO, prepare_merchant_message(user, merchant_id))

        discount_settings: DiscountSetting = DiscountCodeSQL.get_discount_code_settings(merchant_id)

        valid_until = datetime.utcnow() + timedelta(days=discount_settings.discount_code_validity_in_days)
        return CustomResponse.ok_with_kwargs(discount_code=discount_code, valid_until=valid_until)
