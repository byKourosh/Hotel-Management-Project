from data_access.payment_da import PaymentDa

class PaymentBL:
    def __init__(self):
        self.da = PaymentDa()

    def save(self, payment):
        for p in self.da.find_all():
            if p.payment_id == payment.payment_id:
                raise ValueError("Payment ID already exists")
        self.da.save(payment)

    def get_all(self):
        return self.da.find_all()

    def find_by_id(self, payment_id):
        return self.da.find_by_id(payment_id)

    def delete_by_id(self, payment_id):
        self.da.delete_by_id(payment_id)