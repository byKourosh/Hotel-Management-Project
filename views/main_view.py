import tkinter as tk
from views.guest_view import open_guest_window
from views.room_view import open_room_window
from views.reservation_view import open_reservation_window
from views.employee_view import open_employee_window

def run_hotel_app(app_controller):
    win = tk.Tk()
    win.title("Hotel Management System")
    win.geometry("450x400")

    tk.Label(win, text="Hotel Management", font=("Arial", 18, "bold")).pack(pady=30)

    tk.Button(
        win, text="Manage Guests", width=25, font=("Arial", 12),
        command=lambda: open_guest_window(win, app_controller)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Rooms", width=25, font=("Arial", 12),
        command=lambda: open_room_window(win, app_controller)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Reservations", width=25, font=("Arial", 12),
        command=lambda: open_reservation_window(win, app_controller)
    ).pack(pady=10)

    tk.Button(
        win, text="Manage Employees", width=25, font=("Arial", 12),
        command=lambda: open_employee_window(win, app_controller)
    ).pack(pady=10)

    win.mainloop()