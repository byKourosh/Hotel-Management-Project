from .employee import Employee
from tools.validation import shift_validator

class Receptionist(Employee):
    def __init__(self, employee_id: str, name: str, phone: str, salary: float, shift: str):
        super().__init__(employee_id, name, phone, salary)
        self.shift = shift

    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, value: str):
        shift_validator(value)
        self.__shift = value

    def check_in(self, reservation):
        reservation.status = "Checked-In"
        reservation.room.update_status("Occupied")
        print(f"Guest checked in to room {reservation.room.room_number}")

    def check_out(self, reservation):
        reservation.status = "Completed"
        reservation.room.update_status("Available")
        print(f"Guest checked out of room {reservation.room.room_number}")

    def __repr__(self):
        return f"Receptionist({self.employee_id}, {self.name})"