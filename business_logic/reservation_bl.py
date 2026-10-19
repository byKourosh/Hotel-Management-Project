from data_access.reservation_da import ReservationDa

class ReservationBL:
    def __init__(self):
        self.da = ReservationDa()

    def save(self, reservation):
        for r in self.da.find_all():
            if r.reservation_id == reservation.reservation_id:
                raise ValueError("Reservation ID already exists")
        self.da.save(reservation)

    def get_all(self):
        return self.da.find_all()

    def find_by_id(self, reservation_id):
        return self.da.find_by_id(reservation_id)

    def delete_by_id(self, reservation_id):
        self.da.delete_by_id(reservation_id)