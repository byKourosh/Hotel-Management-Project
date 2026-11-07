from models.guest import Guest
from models.room import Room
from models.receptionist import Receptionist
from models.reservation import Reservation
from models.payment import Payment
from models.hotel import Hotel


class HotelSystemController:
    def __init__(self, guest_bl, room_bl, employee_bl, reservation_bl, payment_bl, hotel_bl):
        self.guest_bl = guest_bl
        self.room_bl = room_bl
        self.employee_bl = employee_bl
        self.reservation_bl = reservation_bl
        self.payment_bl = payment_bl
        self.hotel_bl = hotel_bl

    def save_guest(self, guest_id, name, phone, email):
        try:
            self.guest_bl.save(Guest(guest_id, name, phone, email))
            return True, "Guest saved."
        except Exception as e:
            return False, str(e)

    def get_all_guests(self):
        return self.guest_bl.get_all()

    def save_room(self, room_number, room_type, price, status):
        try:
            self.room_bl.save(Room(room_number, room_type, price, status))
            return True, "Room saved."
        except Exception as e:
            return False, str(e)

    def get_all_rooms(self):
        return self.room_bl.get_all()

    def save_employee(self, emp_id, name, phone, salary, shift):
        try:
            self.employee_bl.save(Receptionist(emp_id, name, phone, salary, shift))
            return True, "Employee saved."
        except Exception as e:
            return False, str(e)

    def get_all_employees(self):
        return self.employee_bl.get_all()

    def save_reservation(self, res_id, guest, room, check_in, check_out, status):
        try:
            self.reservation_bl.save(Reservation(res_id, guest, room, check_in, check_out, status))
            return True, "Reservation saved."
        except Exception as e:
            return False, str(e)

    def get_all_reservations(self):
        return self.reservation_bl.get_all()

    def cancel_reservation(self, res_id):
        try:
            self.reservation_bl.delete_by_id(res_id)
            return True, "Reservation cancelled."
        except Exception as e:
            return False, str(e)

    def save_payment(self, pay_id, amount, date, method, status):
        try:
            self.payment_bl.save(Payment(pay_id, amount, date, method, status))
            return True, "Payment saved."
        except Exception as e:
            return False, str(e)

    def save_hotel(self, hotel_id, name, address, phone):
        try:
            self.hotel_bl.save(Hotel(hotel_id, name, address, phone))
            return True, "Hotel saved."
        except Exception as e:
            return False, str(e)