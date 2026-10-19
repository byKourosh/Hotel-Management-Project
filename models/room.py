from tools.validation import room_number_validator, room_type_validator, price_validator, status_validator

class Room:
    def __init__(self, room_number: str, room_type: str, price_per_night: float, status: str = "Available"):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.status = status

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, value: str):
        room_number_validator(value)
        self.__room_number = value

    @property
    def room_type(self):
        return self.__room_type

    @room_type.setter
    def room_type(self, value: str):
        room_type_validator(value)
        self.__room_type = value

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value: float):
        price_validator(value)
        self.__price_per_night = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def get_room_info(self):
        return f"Room {self.room_number} | Type: {self.room_type} | Price: ${self.price_per_night:.2f} | Status: {self.status}"

    def is_available(self):
        return self.status == "Available"

    def update_status(self, new_status: str):
        self.status = new_status
        print(f"Room {self.room_number} status updated to: {self.status}")