import re
from datetime import date

def room_number_validator(room_number):
    if not isinstance(room_number, str) or not re.match(r"^[a-zA-Z0-9\-]{3,10}$", room_number):
        raise ValueError("Invalid Room Number")
    return room_number

def room_type_validator(room_type):
    if not isinstance(room_type, str) or not re.match(r"^[a-zA-Z\s]{3,30}$", room_type):
        raise ValueError("Invalid Room Type")
    return room_type

def price_validator(price):
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid Price")
    return price

def status_validator(status):
    if not isinstance(status, str) or len(status) < 3:
        raise ValueError("Invalid Status")
    return status

def guest_id_validator(guest_id):
    if not isinstance(guest_id, str) or not re.match(r"^G\d{5}$", guest_id):
        raise ValueError("Invalid Guest ID")
    return guest_id

def reservation_id_validator(reservation_id):
    if not isinstance(reservation_id, str) or not re.match(r"^R\d{5}$", reservation_id):
        raise ValueError("Invalid Reservation ID")
    return reservation_id

def payment_id_validator(payment_id):
    if not isinstance(payment_id, str) or not re.match(r"^P\d{5}$", payment_id):
        raise ValueError("Invalid Payment ID")
    return payment_id

def name_validator(name):
    if not isinstance(name, str) or not re.match(r"^[a-zA-Z\s]{3,50}$", name):
        raise ValueError("Invalid Name")
    return name

def phone_validator(phone):
    if not isinstance(phone, str) or not re.match(r"^\d{10,15}$", phone):
        raise ValueError("Invalid Phone Number")
    return phone

def email_validator(email):
    if not isinstance(email, str) or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("Invalid Email")
    return email

def date_validator(value):
    if not isinstance(value, date):
        raise ValueError("Invalid Date")
    return value

def amount_validator(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid Amount")
    return amount

def payment_method_validator(method):
    if not isinstance(method, str) or not re.match(r"^[a-zA-Z\s]{3,30}$", method):
        raise ValueError("Invalid Payment Method")
    return method
def hotel_id_validator(hotel_id):
    if not isinstance(hotel_id, str) or not re.match(r"^H\d{3,5}$", hotel_id):
        raise ValueError("Invalid Hotel ID")
    return hotel_id

def address_validator(address):
    if not isinstance(address, str) or len(address) < 5:
        raise ValueError("Invalid Address")
    return address

def employee_id_validator(employee_id):
    if not isinstance(employee_id, str) or not re.match(r"^E\d{4,6}$", employee_id):
        raise ValueError("Invalid Employee ID")
    return employee_id

def salary_validator(salary):
    if not isinstance(salary, (int, float)) or salary < 0:
        raise ValueError("Invalid Salary")
    return salary

def shift_validator(shift):
    if not isinstance(shift, str) or len(shift) < 3:
        raise ValueError("Invalid Shift")
    return shift