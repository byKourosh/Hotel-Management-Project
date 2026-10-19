import tkinter as tk
from tkinter import ttk, messagebox
from models.receptionist import Receptionist


def open_employee_window(parent, employees_list):
    window = tk.Toplevel(parent)
    window.title("Employee Management")
    window.geometry("850x500")

    def refresh_table():
        for item in table.get_children():
            table.delete(item)
        for e in employees_list:
            table.insert("", "end", values=(e.employee_id, e.name, e.phone, f"${e.salary:.2f}", e.shift))

    def save_employee():
        try:
            salary_val = float(salary_entry.get().strip())

            new_emp = Receptionist(
                employee_id=id_entry.get().strip(),
                name=name_entry.get().strip(),
                phone=phone_entry.get().strip(),
                salary=salary_val,
                shift=shift_entry.get().strip()
            )
            employees_list.append(new_emp)
            refresh_table()
            messagebox.showinfo("Success", "Receptionist added successfully!")

            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            salary_entry.delete(0, tk.END)
            shift_entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

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