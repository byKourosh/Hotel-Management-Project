from .validation import hotel_id_validator, name_validator, address_validator, phone_validator
from .room import Room

class Hotel:
    def __init__(self, hotel_id: str, name: str, address: str, phone: str):
        self.hotelId = hotel_id
        self.name = name
        self.address = address
        self.phone = phone
        self.__rooms = []

    @property
    def hotelId(self) -> str:
        return self.__hotelId

    @hotelId.setter
    def hotelId(self, value: str):
        hotel_id_validator(value)
        self.__hotelId = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str):
        address_validator(value)
        self.__address = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        phone_validator(value)
        self.__phone = value

    def addRoom(self, room: Room) -> None:
        self.__rooms.append(room)

    def getAvailableRooms(self) -> list:
        return [room for room in self.__rooms if room.isAvailable()]

    def getHotelInfo(self) -> str:
        return f"Hotel {self.name} (ID: {self.hotelId}) | Address: {self.address} | Phone: {self.phone}"