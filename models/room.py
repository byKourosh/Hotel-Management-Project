from .validation import room_number_validator, room_type_validator, price_validator, status_validator

class Room:
    def __init__(self, room_number: str, room_type: str, price_per_night: float, status: str = "Available"):
        self.roomNumber = room_number
        self.roomType = room_type
        self.pricePerNight = price_per_night
        self.status = status

    @property
    def roomNumber(self) -> str:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, value: str):
        room_number_validator(value)
        self.__roomNumber = value

    @property
    def roomType(self) -> str:
        return self.__roomType

    @roomType.setter
    def roomType(self, value: str):
        room_type_validator(value)
        self.__roomType = value

    @property
    def pricePerNight(self) -> float:
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, value: float):
        price_validator(value)
        self.__pricePerNight = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        status_validator(value)
        self.__status = value

    def getRoomInfo(self) -> str:
        return f"Room {self.roomNumber} | Type: {self.roomType} | Price: ${self.pricePerNight:.2f} | Status: {self.status}"

    def isAvailable(self) -> bool:
        return self.status == "Available"

    def updateStatus(self, new_status: str) -> None:
        self.status = new_status
        print(f"Room {self.roomNumber} status updated to: {self.status}")