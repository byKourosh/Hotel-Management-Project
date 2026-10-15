from .validation import employee_id_validator, name_validator, phone_validator, salary_validator

class Employee:
    def __init__(self, employee_id: str, name: str, phone: str, salary: float):
        self.employeeId = employee_id
        self.name = name
        self.phone = phone
        self.salary = salary

    @property
    def employeeId(self) -> str:
        return self.__employeeId

    @employeeId.setter
    def employeeId(self, value: str):
        employee_id_validator(value)
        self.__employeeId = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        phone_validator(value)
        self.__phone = value

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        salary_validator(value)
        self.__salary = value

    def getEmployeeInfo(self) -> str:
        return f"Employee {self.name} (ID: {self.employeeId}) | Phone: {self.phone} | Salary: ${self.salary:.2f}"

    def updateEmployeeInfo(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)