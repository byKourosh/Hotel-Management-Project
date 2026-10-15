from .employee import Employee
from .validation import shift_validator

class Receptionist(Employee):
    def __init__(self, employee_id: str, name: str, phone: str, salary: float, shift: str):
        super().__init__(employee_id, name, phone, salary)
        self.shift = shift

    @property
    def shift(self) -> str:
        return self.__shift

    @shift.setter
    def shift(self, value: str):
        shift_validator(value)
        self.__shift = value

    def checkIn(self) -> None:
        pass

    def checkOut(self) -> None:
        pass