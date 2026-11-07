class HotelDa:
    def __init__(self):
        self.hotel_list = []

    def save(self, hotel):
        self.hotel_list.append(hotel)

    def find_all(self):
        return self.hotel_list

    def find_by_id(self, hotel_id):
        for h in self.hotel_list:
            if h.hotel_id == hotel_id:
                return h
        return None

    def delete_by_id(self, hotel_id):
        for h in self.hotel_list:
            if h.hotel_id == hotel_id:
                self.hotel_list.remove(h)
                return