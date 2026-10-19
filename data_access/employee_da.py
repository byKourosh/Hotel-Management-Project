class EmployeeDa:
    def __init__(self):
        self.employee_list = []

    def save(self, employee):
        self.employee_list.append(employee)

    def find_all(self):
        return self.employee_list

    def find_by_id(self, employee_id):
        for e in self.employee_list:
            if e.employee_id == employee_id:
                return e
        return None

    def delete_by_id(self, employee_id):
        for e in self.employee_list:
            if e.employee_id == employee_id:
                self.employee_list.remove(e)
                return