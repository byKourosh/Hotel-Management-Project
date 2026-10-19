class RoomDa:
    def __init__(self):
        self.room_list = []

    def save(self, room):
        self.room_list.append(room)

    def find_all(self):
        return self.room_list

    def find_by_number(self, room_number):
        for r in self.room_list:
            if r.room_number == room_number:
                return r
        return None

    def delete_by_number(self, room_number):
        for r in self.room_list:
            if r.room_number == room_number:
                self.room_list.remove(r)
                return