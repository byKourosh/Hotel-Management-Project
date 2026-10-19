import tkinter as tk
from tkinter import ttk, messagebox
from models.room import Room


def open_room_window(parent, rooms_list):
    window = tk.Toplevel(parent)
    window.title("Room Management")
    window.geometry("850x500")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        for r in rooms_list:
            table.insert("", "end", values=(r.room_number, r.room_type, f"${r.price_per_night:.2f}", r.status))

    def save_room():
        try:
            price = float(price_entry.get().strip())
            new_num = num_entry.get().strip()

            for r in rooms_list:
                if r.room_number == new_num:
                    raise ValueError("Room number already exists!")

            new_room = Room(
                room_number=new_num,
                room_type=type_entry.get().strip(),
                price_per_night=price,
                status=status_entry.get().strip()
            )
            rooms_list.append(new_room)
            refresh_table()
            messagebox.showinfo("Success", "Room added successfully!")

            num_entry.delete(0, tk.END)
            type_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            status_entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    form = tk.LabelFrame(window, text="Add Room")
    form.pack(fill="x", padx=10, pady=10)

    tk.Label(form, text="Room Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    num_entry = tk.Entry(form)
    num_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Room Type:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    type_entry = tk.Entry(form)
    type_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Price Per Night:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    price_entry = tk.Entry(form)
    price_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form, text="Status (Available/Occupied):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    status_entry = tk.Entry(form)
    status_entry.insert(0, "Available")
    status_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(form, text="Save Room", command=save_room).grid(row=4, column=0, columnspan=2, pady=10)

    columns = ("room_number", "room_type", "price_per_night", "status")
    table = ttk.Treeview(window, columns=columns, show="headings")

    table.heading("room_number", text="Room Number")
    table.heading("room_type", text="Room Type")
    table.heading("price_per_night", text="Price Per Night")
    table.heading("status", text="Status")

    for col in columns:
        table.column(col, width=150)

    table.pack(fill="both", expand=True, padx=10, pady=10)
    refresh_table()