class PaymentDa:
    def __init__(self):
        self.payment_list = []

    def save(self, payment):
        self.payment_list.append(payment)

    def find_all(self):
        return self.payment_list

    def find_by_id(self, payment_id):
        for p in self.payment_list:
            if p.payment_id == payment_id:
                return p
        return None

    def delete_by_id(self, payment_id):
        for p in self.payment_list:
            if p.payment_id == payment_id:
                self.payment_list.remove(p)
                return