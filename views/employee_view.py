import tkinter as tk
from tkinter import ttk, messagebox

def open_employee_window(parent, app_controller):
    window = tk.Toplevel(parent)
    window.title("Employee Management")
    window.geometry("850x500")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        employees = app_controller.get_all_employees()
        for e in employees:
            table.insert("", "end", values=(e.employee_id, e.name, e.phone, f"${e.salary:.2f}", e.shift))

    def save_employee():
        try:
            salary_val = float(salary_entry.get().strip())
            success, message = app_controller.save_employee(
                id_entry.get().strip(),
                name_entry.get().strip(),
                phone_entry.get().strip(),
                salary_val,
                shift_entry.get().strip()
            )
            if success:
                refresh_table()
                messagebox.showinfo("Success", message)
                id_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                salary_entry.delete(0, tk.END)
                shift_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", message)
        except ValueError:
            messagebox.showerror("Error", "Salary must be a valid number")

    form = tk.LabelFrame(window, text="Register Receptionist (ID format: E1234)")
    form.pack(fill="x", padx=10, pady=10)

    tk.Label(form, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = tk.Entry(form)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    name_entry = tk.Entry(form)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    phone_entry = tk.Entry(form)
    phone_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form, text="Salary:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    salary_entry = tk.Entry(form)
    salary_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(form, text="Shift (Morning/Evening):").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    shift_entry = tk.Entry(form)
    shift_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Button(form, text="Save Employee", command=save_employee).grid(row=5, column=0, columnspan=2, pady=10)

    columns = ("id", "name", "phone", "salary", "shift")
    table = ttk.Treeview(window, columns=columns, show="headings")

    table.heading("id", text="ID")
    table.heading("name", text="Name")
    table.heading("phone", text="Phone")
    table.heading("salary", text="Salary")
    table.heading("shift", text="Shift")

    table.pack(fill="both", expand=True, padx=10, pady=10)
    refresh_table()