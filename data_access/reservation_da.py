class ReservationDa:
    def __init__(self):
        self.reservation_list = []

    def save(self, reservation):
        self.reservation_list.append(reservation)

    def find_all(self):
        return self.reservation_list

    def find_by_id(self, reservation_id):
        for r in self.reservation_list:
            if r.reservation_id == reservation_id:
                return r
        return None

    def delete_by_id(self, reservation_id):
        for r in self.reservation_list:
            if r.reservation_id == reservation_id:
                self.reservation_list.remove(r)
                return