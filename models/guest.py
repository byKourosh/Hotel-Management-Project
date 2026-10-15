from .validation import guest_id_validator, name_validator, phone_validator, email_validator

class Guest:
    def __init__(self, guest_id: str, name: str, phone_number: str, email: str):
        self.guestId = guest_id
        self.name = name
        self.phoneNumber = phone_number
        self.email = email

    @property
    def guestId(self) -> str:
        return self.__guestId

    @guestId.setter
    def guestId(self, value: str):
        guest_id_validator(value)
        self.__guestId = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value: str):
        phone_validator(value)
        self.__phoneNumber = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        email_validator(value)
        self.__email = value

    def createReservation(self):
        pass

    def getReservations(self):
        pass

    def updateProfile(self):
        pass