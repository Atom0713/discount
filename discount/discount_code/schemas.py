import datetime
from decimal import Decimal

from discount import db


class Merchant(db.Model):
    merchant_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)


class User(db.Model):
    user_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)


class DiscountType(db.Model):
    discount_type_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)


class DiscountSetting(db.Model):
    merchant_id: int = db.Column(db.Integer, db.ForeignKey(Merchant.merchant_id), primary_key=True)
    discount_code_validity_in_days: int = db.Column(db.Integer, default=7)
    code_length: int = db.Column(db.Integer, default=12)
    code_origin: str = db.Column(db.String(50), default="ABCDEFGHIJKLMNOPQRST1234567890")


class Discount(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    code: str = db.Column(db.String(50), nullable=False)
    value: Decimal = db.Column(db.DECIMAL(19, 6), nullable=False)
    discount_type_id: int = db.Column(db.Integer, db.ForeignKey(DiscountType.discount_type_id))
    merchant_id: int = db.Column(db.Integer, db.ForeignKey(Merchant.merchant_id), nullable=False)
    reserved_by: int = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=True)
    reservation_date: datetime = db.Column(db.DateTime, nullable=True)
    is_used: bool = db.Column(db.Boolean, default=False)
    creation_date: datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            'code': self.code,
            'value': self.value,
            'discount_type': DiscountType.query.get(self.discount_type_id).name,
            'creation_date': self.creation_date
        }


