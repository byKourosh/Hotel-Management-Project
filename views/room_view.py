import tkinter as tk
from tkinter import ttk, messagebox

def open_room_window(parent, app_controller):
    window = tk.Toplevel(parent)
    window.title("Room Management")
    window.geometry("850x500")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        rooms = app_controller.get_all_rooms()
        for r in rooms:
            table.insert("", "end", values=(r.room_number, r.room_type, f"${r.price_per_night:.2f}", r.status))

    def save_room():
        try:
            price = float(price_entry.get().strip())
            success, message = app_controller.save_room(
                num_entry.get().strip(),
                type_entry.get().strip(),
                price,
                status_entry.get().strip()
            )
            if success:
                refresh_table()
                messagebox.showinfo("Success", message)
                num_entry.delete(0, tk.END)
                type_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
                status_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", message)
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number")

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