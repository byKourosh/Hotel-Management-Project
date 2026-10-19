from tools.validation import employee_id_validator, name_validator, phone_validator, salary_validator

class Employee:
    def __init__(self, employee_id: str, name: str, phone: str, salary: float):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value: str):
        employee_id_validator(value)
        self.__employee_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        name_validator(value)
        self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        phone_validator(value)
        self.__phone = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        salary_validator(value)
        self.__salary = value

    def get_employee_info(self):
        return f"Employee {self.name} (ID: {self.employee_id}) | Phone: {self.phone} | Salary: ${self.salary:.2f}"

    #ostad farmodid in ro hazf konam vali chon dakhel UML ke shoma tayid farmodid bodan,man be sorat sade tar neveshtameshon.
    def update_employee_info(self, name=None, phone=None, salary=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if salary:
            self.salary = salary