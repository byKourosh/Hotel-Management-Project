import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from business_logic.employee_bl import EmployeeBL
from business_logic.guest_bl import GuestBL
from business_logic.hotel_bl import HotelBL
from business_logic.payment_bl import PaymentBL
from business_logic.reservation_bl import ReservationBL
from business_logic.room_bl import RoomBL

from controller.controller import HotelSystemController
from views.main_view import run_hotel_app

def main():
    guest_bl = GuestBL()
    room_bl = RoomBL()
    employee_bl = EmployeeBL()
    reservation_bl = ReservationBL()
    payment_bl = PaymentBL()
    hotel_bl = HotelBL()

    app_controller = HotelSystemController(
        guest_bl, room_bl, employee_bl, reservation_bl, payment_bl, hotel_bl
    )

    run_hotel_app(app_controller)

if __name__ == "__main__":
    main()