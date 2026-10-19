from datetime import date
from tools.validation import reservation_id_validator, date_validator, status_validator

class Reservation:
    def __init__(self, reservation_id: str, guest, room, check_in_date: date, check_out_date: date, status: str):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    @property
    def reservation_id(self):
        return self.__reservation_id

    @reservation_id.setter
    def reservation_id(self, value: str):
        reservation_id_validator(value)
        self.__reservation_id = value

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value: date):
        date_validator(value)
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value: date):
        date_validator(value)
        self.__check_out_date = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def calculate_total(self):
        days = (self.check_out_date - self.check_in_date).days
        return days * self.room.price_per_night

    def confirm_reservation(self):
        self.status = "Confirmed"

    def cancel_reservation(self):
        self.status = "Cancelled"
        self.room.update_status("Available")

    def __repr__(self):
        return f"Reservation({self.reservation_id}, {self.guest.name}, {self.room.room_number})"