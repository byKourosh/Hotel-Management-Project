from datetime import date
from tools.validation import payment_id_validator, amount_validator, date_validator, payment_method_validator, status_validator

class Payment:
    def __init__(self, payment_id: str, amount: float, payment_day: date, payment_method: str, status: str):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_day = payment_day
        self.payment_method = payment_method
        self.status = status

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str):
        payment_id_validator(value)
        self.__payment_id = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        amount_validator(value)
        self.__amount = value

    @property
    def payment_day(self):
        return self.__payment_day

    @payment_day.setter
    def payment_day(self, value: date):
        date_validator(value)
        self.__payment_day = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: str):
        payment_method_validator(value)
        self.__payment_method = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def process_payment(self):
        pass

    def get_payment_details(self):
        pass