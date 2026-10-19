import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from views.guest_view import open_guest_window
from views.room_view import open_room_window
from views.reservation_view import open_reservation_window
from views.employee_view import open_employee_window


def run_hotel_app():
    guests_list = []
    rooms_list = []
    reservations_list = []
    employees_list = []

    win = tk.Tk()
    win.title("Hotel Management System")
    win.geometry("450x400")

    tk.Label(win, text="Hotel Management", font=("Arial", 18, "bold")).pack(pady=30)

    tk.Button(
        win, text="Manage Guests", width=25, font=("Arial", 12),
        command=lambda: open_guest_window(win, guests_list)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Rooms", width=25, font=("Arial", 12),
        command=lambda: open_room_window(win, rooms_list)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Reservations", width=25, font=("Arial", 12),
        command=lambda: open_reservation_window(win, reservations_list, guests_list, rooms_list)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Employees", width=25, font=("Arial", 12),
        command=lambda: open_employee_window(win, employees_list)
    ).pack(pady=10)

    win.mainloop()


if __name__ == "__main__":
    run_hotel_app()