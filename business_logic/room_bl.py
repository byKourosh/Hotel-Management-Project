from data_access.room_da import RoomDa

class RoomBL:
    def __init__(self):
        self.da = RoomDa()

    def save(self, room):
        for r in self.da.find_all():
            if r.room_number == room.room_number:
                raise ValueError("Room number already exists")
        self.da.save(room)

    def get_all(self):
        return self.da.find_all()

    def find_by_number(self, room_number):
        return self.da.find_by_number(room_number)

    def delete_by_number(self, room_number):
        self.da.delete_by_number(room_number)