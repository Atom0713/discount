import datetime
from typing import List

from werkzeug.exceptions import abort

from discount import db, logger
from discount.discount_code.schemas import DiscountSetting, Discount


class DiscountCodeSQL:

    @staticmethod
    def get_discount_code_settings(merchant_id: int) -> 'DiscountSetting':
        return DiscountSetting.query.get(merchant_id)

    @staticmethod
    def get_all_active_discount_codes_by_merchant(merchant_id: int) -> List[dict]:
        all_active_codes: List[Discount] = Discount.query\
            .filter(Discount.merchant_id == merchant_id) \
            .filter(Discount.is_used == 0) \
            .filter(Discount.reserved_by == None) \
            .all()
        return [i.to_json() for i in all_active_codes]

    @staticmethod
    def save_discount_codes(discount_config: list):
        session = db.session
        try:
            new_discounts: List[Discount] = [Discount(**discount) for discount in discount_config]

            session.add_all(new_discounts)
            session.commit()

        except Exception as err:
            session.rollback()
            logger.exception(err)
            abort(500)

    @staticmethod
    def get_and_reserve_discount_code(user_id: int, merchant_id: int):
        try:
            discount_code: Discount = Discount.query\
                .filter(Discount.merchant_id == merchant_id) \
                .filter(Discount.is_used == 0) \
                .filter(Discount.reserved_by == None) \
                .first()

            if not discount_code:
                return None

            discount_code.reserved_by = user_id
            discount_code.reservation_date = datetime.datetime.utcnow()
            db.session.commit()

            return discount_code.code

        except Exception as err:
            logger.exception(err)
            abort(500)



