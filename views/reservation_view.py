import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from models.reservation import Reservation


def open_reservation_window(parent, reservations_list, guests_list, rooms_list):
    window = tk.Toplevel(parent)
    window.title("Reservation Management")
    window.geometry("900x550")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        for r in reservations_list:
            table.insert("", "end", values=(r.reservationId, str(r.checkInDate), str(r.checkOutDate), r.status))

    def update_dropdowns():
        guest_box['values'] = [g.guestId for g in guests_list]
        room_box['values'] = [r.roomNumber for r in rooms_list]

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

            selected_guest = next((g for g in guests_list if g.guestId == selected_guest_id), None)
            selected_room = next((r for r in rooms_list if r.roomNumber == selected_room_id), None)

            if selected_room.status != "Available":
                raise ValueError("Room is not available")

            new_res = Reservation(
                reservation_id=res_id_entry.get().strip(),
                guest=selected_guest,
                room=selected_room,
                check_in_date=check_in,
                check_out_date=check_out,
                status=status_entry.get().strip()
            )

            reservations_list.append(new_res)
            selected_room.updateStatus("Occupied")

            refresh_table()
            update_dropdowns()
            messagebox.showinfo("Success", "Reservation created!")

            res_id_entry.delete(0, tk.END)
            in_date_entry.delete(0, tk.END)
            out_date_entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cancel_selected_reservation():
        selected = table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a reservation from the table")
            return

        res_id = table.item(selected[0], "values")[0]
        for res in reservations_list:
            if res.reservationId == res_id:
                res.cancelReservation()
                reservations_list.remove(res)
                break
        refresh_table()
        update_dropdowns()
        messagebox.showinfo("Success", "Reservation cancelled")

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

    tk.Button(form, text="Book Reservation", command=save_reservation).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(form, text="Cancel Selected", command=cancel_selected_reservation).grid(row=4, column=2, columnspan=2,
                                                                                      pady=10)

    columns = ("id", "checkin", "checkout", "status")
    table = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col.capitalize())
        table.column(col, width=200)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    refresh_table()
    update_dropdowns()