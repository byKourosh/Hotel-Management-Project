class GuestDa:
    def __init__(self):
        self.guest_list = []

    def save(self, guest):
        self.guest_list.append(guest)

    def find_all(self):
        return self.guest_list

    def find_by_id(self, guest_id):
        for g in self.guest_list:
            if g.guest_id == guest_id:
                return g
        return None

    def delete_by_id(self, guest_id):
        for g in self.guest_list:
            if g.guest_id == guest_id:
                self.guest_list.remove(g)
                return