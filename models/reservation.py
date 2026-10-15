from datetime import date
from .validation import reservation_id_validator, date_validator, status_validator

class Reservation:
    def __init__(self, reservation_id: str, check_in_date: date, check_out_date: date, status: str):
        self.reservationId = reservation_id
        self.checkInDate = check_in_date
        self.checkOutDate = check_out_date
        self.status = status

    @property
    def reservationId(self) -> str:
        return self.__reservationId

    @reservationId.setter
    def reservationId(self, value: str):
        reservation_id_validator(value)
        self.__reservationId = value

    @property
    def checkInDate(self) -> date:
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, value: date):
        date_validator(value)
        self.__checkInDate = value

    @property
    def checkOutDate(self) -> date:
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, value: date):
        date_validator(value)
        self.__checkOutDate = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def calculateTotal(self):
        pass

    def confirmReservation(self):
        pass

    def cancelReservation(self):
        pass