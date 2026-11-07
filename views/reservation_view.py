import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date


def open_reservation_window(parent, app_controller):
    window = tk.Toplevel(parent)
    window.title("Reservation Management")
    window.geometry("900x550")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        reservations = app_controller.get_all_reservations()
        for r in reservations:
            table.insert(
                "", "end",
                values=(r.reservation_id, str(r.check_in_date), str(r.check_out_date), r.status)
            )

    def update_dropdowns():
        guests = app_controller.get_all_guests()
        rooms = app_controller.get_all_rooms()

        # Only show available rooms in the dropdown
        available_rooms = [r for r in rooms if r.status == "Available"]

        guest_box['values'] = [g.guest_id for g in guests]
        room_box['values'] = [r.room_number for r in available_rooms]

    def save_reservation():
        try:
            selected_guest_id = guest_box.get()
            selected_room_id = room_box.get()

            if not selected_guest_id or not selected_room_id:
                raise ValueError("Please select a Guest and a Room")

            check_in = date.fromisoformat(in_date_entry.get().strip())
            check_out = date.fromisoformat(out_date_entry.get().strip())

            if check_out <= check_in:
                raise ValueError("Check-out date must be after Check-in date")

            # Find the actual Guest and Room objects via the controller
            selected_guest = None
            for g in app_controller.get_all_guests():
                if g.guest_id == selected_guest_id:
                    selected_guest = g
                    break

            selected_room = None
            for r in app_controller.get_all_rooms():
                if r.room_number == selected_room_id:
                    selected_room = r
                    break

            if not selected_guest or not selected_room:
                raise ValueError("Guest or Room not found")

            if selected_room.status != "Available":
                raise ValueError("Room is not available")

            success, message = app_controller.save_reservation(
                res_id_entry.get().strip(),
                selected_guest,
                selected_room,
                check_in,
                check_out,
                status_entry.get().strip()
            )

            if success:
                selected_room.update_status("Occupied")
                refresh_table()
                update_dropdowns()
                messagebox.showinfo("Success", message)
                res_id_entry.delete(0, tk.END)
                in_date_entry.delete(0, tk.END)
                out_date_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", message)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_selected_reservation():
        selected = table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a reservation from the table")
            return

        res_id = table.item(selected[0], "values")[0]

        # Find the reservation to free the room
        for res in app_controller.get_all_reservations():
            if res.reservation_id == res_id:
                res.cancel_reservation()
                break

        success, message = app_controller.cancel_reservation(res_id)
        if success:
            refresh_table()
            update_dropdowns()
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    form = tk.LabelFrame(window, text="Book Reservation (ID format: R12345)")
    form.pack(fill="x", padx=10, pady=10)

    tk.Label(form, text="Reservation ID:").grid(row=0, column=0, padx=5, pady=5)
    res_id_entry = tk.Entry(form)
    res_id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Select Guest:").grid(row=1, column=0, padx=5, pady=5)
    guest_box = ttk.Combobox(form, state="readonly")
    guest_box.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Select Room:").grid(row=1, column=2, padx=5, pady=5)
    room_box = ttk.Combobox(form, state="readonly")
    room_box.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(form, text="Check-In (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
    in_date_entry = tk.Entry(form)
    in_date_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form, text="Check-Out (YYYY-MM-DD):").grid(row=2, column=2, padx=5, pady=5)
    out_date_entry = tk.Entry(form)
    out_date_entry.grid(row=2, column=3, padx=5, pady=5)

    tk.Label(form, text="Status:").grid(row=3, column=0, padx=5, pady=5)
    status_entry = tk.Entry(form)
    status_entry.insert(0, "Confirmed")
    status_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(form, text="Book Reservation", command=save_reservation).grid(
        row=4, column=0, columnspan=2, pady=10
    )
    tk.Button(form, text="Cancel Selected", command=cancel_selected_reservation).grid(
        row=4, column=2, columnspan=2, pady=10
    )

    columns = ("id", "check_in", "check_out", "status")
    table = ttk.Treeview(window, columns=columns, show="headings")

    table.heading("id", text="ID")
    table.heading("check_in", text="Check In")
    table.heading("check_out", text="Check Out")
    table.heading("status", text="Status")

    for col in columns:
        table.column(col, width=200)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    refresh_table()
    update_dropdowns()