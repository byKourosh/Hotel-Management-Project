from tools.validation import guest_id_validator, name_validator, phone_validator, email_validator

class Guest:
    def __init__(self, guest_id: str, name: str, phone_number: str, email: str):
        self.guest_id = guest_id
        self.name = name
        self.phone_number = phone_number
        self.email = email

    @property
    def guest_id(self):
        return self.__guest_id

    @guest_id.setter
    def guest_id(self, value: str):
        guest_id_validator(value)
        self.__guest_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        phone_validator(value)
        self.__phone_number = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        email_validator(value)
        self.__email = value

    def __repr__(self):
        return f"Guest({self.guest_id}, {self.name})"

    # ostad farmodid in ro hazf konam vali chon dakhel UML ke shoma tayid farmodid bodan,man be sorat sade tar neveshtameshon.
    def create_reservation(self):
        pass

    def get_reservations(self):
        pass

    def update_profile(self):
        pass