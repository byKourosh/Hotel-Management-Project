import tkinter as tk
from tkinter import ttk, messagebox
from models.guest import Guest


def open_guest_window(parent, guests_list):
    window = tk.Toplevel(parent)
    window.title("Guest Management")
    window.geometry("850x500")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        for g in guests_list:
            table.insert("", "end", values=(g.guestId, g.name, g.phoneNumber, g.email))

    def save_guest():
        try:
            new_guest = Guest(
                guest_id=id_entry.get().strip(),
                name=name_entry.get().strip(),
                phone_number=phone_entry.get().strip(),
                email=email_entry.get().strip()
            )
            guests_list.append(new_guest)
            refresh_table()
            messagebox.showinfo("Success", "Guest added successfully!")

            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    form = tk.LabelFrame(window, text="Register Guest (ID format: G12345)")
    form.pack(fill="x", padx=10, pady=10)

    tk.Label(form, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = tk.Entry(form)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = tk.Entry(form)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Phone (10-15 digits):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    phone_entry = tk.Entry(form)
    phone_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    email_entry = tk.Entry(form)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(form, text="Save Guest", command=save_guest).grid(row=4, column=0, columnspan=2, pady=10)

    columns = ("id", "name", "phone", "email")
    table = ttk.Treeview(window, columns=columns, show="headings")

    table.heading("id", text="Guest ID")
    table.heading("name", text="Name")
    table.heading("phone", text="Phone")
    table.heading("email", text="Email")

    table.column("id", width=100)
    table.column("name", width=200)
    table.column("phone", width=150)
    table.column("email", width=200)

    table.pack(fill="both", expand=True, padx=10, pady=10)
    refresh_table()