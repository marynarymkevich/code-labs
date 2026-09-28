from Models.room import Room

rooms = [
    Room(101, "Single", 1),
    Room(102, "Single", 1),
    Room(103, "Double", 2),
    Room(104, "Double", 2),
    Room(201, "Suite", 3),
    Room(202, "Family Suite", 4),
    Room(203, "Penthouse", 5)
]


print(f"Welcome, dear customer. Below you can see all our available room. Please enter the room number you want to book. ")
print(f"\n")