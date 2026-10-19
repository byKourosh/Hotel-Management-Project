from models.guest import Guest
from models.room import Room
from models.receptionist import Receptionist
from models.reservation import Reservation
from datetime import date

guest1 = Guest("G12345", "John Doe", "09123456789", "john@example.com")
guest2 = Guest("G12346", "Jane Smith", "09876543210", "jane@example.com")
print(guest1)
print(guest2)

room1 = Room("101", "Single", 150.0, "Available")
room2 = Room("102", "Double", 250.0, "Available")
print(room1)
print(room2)

emp1 = Receptionist("E1234", "Alice Brown", "09121112222", 3000.0, "Morning")
emp2 = Receptionist("E1235", "Bob White", "09123334444", 3500.0, "Evening")
print(emp1)
print(emp2)

check_in = date(2026, 11, 1)
check_out = date(2026, 11, 5)
res1 = Reservation("R12345", guest1, room1, check_in, check_out, "Confirmed")
print(res1)