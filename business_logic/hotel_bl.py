from data_access.hotel_da import HotelDa

class HotelBL:
    def __init__(self):
        self.da = HotelDa()

    def save(self, hotel):
        for h in self.da.find_all():
            if h.hotel_id == hotel.hotel_id:
                raise ValueError("Hotel ID already exists")
        self.da.save(hotel)

    def get_all(self):
        return self.da.find_all()

    def find_by_id(self, hotel_id):
        return self.da.find_by_id(hotel_id)

    def delete_by_id(self, hotel_id):
        self.da.delete_by_id(hotel_id)