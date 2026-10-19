from data_access.guest_da import GuestDa

class GuestBL:
    def __init__(self):
        self.da = GuestDa()

    def save(self, guest):
        for g in self.da.find_all():
            if g.guest_id == guest.guest_id:
                raise ValueError("Guest ID already exists")
        self.da.save(guest)

    def get_all(self):
        return self.da.find_all()

    def find_by_id(self, guest_id):
        return self.da.find_by_id(guest_id)

    def delete_by_id(self, guest_id):
        self.da.delete_by_id(guest_id)