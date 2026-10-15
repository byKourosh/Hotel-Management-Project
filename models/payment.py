from datetime import date
from .validation import payment_id_validator, amount_validator, date_validator, payment_method_validator, status_validator

class Payment:
    def __init__(self, payment_id: str, amount: float, payment_day: date, payment_method: str, status: str):
        self.paymentId = payment_id
        self.amount = amount
        self.paymentDay = payment_day
        self.paymentMethod = payment_method
        self.status = status

    @property
    def paymentId(self) -> str:
        return self.__paymentId

    @paymentId.setter
    def paymentId(self, value: str):
        payment_id_validator(value)
        self.__paymentId = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        amount_validator(value)
        self.__amount = value

    @property
    def paymentDay(self) -> date:
        return self.__paymentDay

    @paymentDay.setter
    def paymentDay(self, value: date):
        date_validator(value)
        self.__paymentDay = value

    @property
    def paymentMethod(self) -> str:
        return self.__paymentMethod

    @paymentMethod.setter
    def paymentMethod(self, value: str):
        payment_method_validator(value)
        self.__paymentMethod = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def processPayment(self):
        pass

    def getPaymentDetails(self):
        pass