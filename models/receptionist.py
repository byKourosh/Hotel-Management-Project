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

    def checkIn(self, reservation):
        reservation.status = "Checked-In"
        reservation.room.updateStatus("Occupied")
        print(f"Guest checked in to room {reservation.room.roomNumber}")

    def checkOut(self, reservation):
        reservation.status = "Completed"
        reservation.room.updateStatus("Available")
        print(f"Guest checked out of room {reservation.room.roomNumber}")

    def __repr__(self):
        return f"Receptionist({self.employeeId}, {self.name})"