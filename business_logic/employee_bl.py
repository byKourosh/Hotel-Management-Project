from data_access.employee_da import EmployeeDa

class EmployeeBL:
    def __init__(self):
        self.da = EmployeeDa()

    def save(self, employee):
        for e in self.da.find_all():
            if e.employee_id == employee.employee_id:
                raise ValueError("Employee ID already exists")
        self.da.save(employee)

    def get_all(self):
        return self.da.find_all()

    def find_by_id(self, employee_id):
        return self.da.find_by_id(employee_id)

    def delete_by_id(self, employee_id):
        self.da.delete_by_id(employee_id)