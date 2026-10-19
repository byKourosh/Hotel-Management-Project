from tools.validation import hotel_id_validator, name_validator, address_validator, phone_validator
from .room import Room

class Hotel:
    def __init__(self, hotel_id: str, name: str, address: str, phone: str):
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.phone = phone
        self.__rooms = []

    @property
    def hotel_id(self):
        return self.__hotel_id

    @hotel_id.setter
    def hotel_id(self, value: str):
        hotel_id_validator(value)
        self.__hotel_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        address_validator(value)
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        phone_validator(value)
        self.__phone = value

    def add_room(self, room: Room):
        self.__rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.__rooms if room.is_available()]

    def get_hotel_info(self):
        return f"Hotel {self.name} (ID: {self.hotel_id}) | Address: {self.address} | Phone: {self.phone}"