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

available_rooms = [room for room in rooms if room.get_availability()]


print(f"\n***Welcome, dear customer. Below you can see all our available rooms. Please enter the room number you want to book.***\n")
for room in available_rooms:
    print(f"{room}")

selected_number = int(input("Enter room number: "))

for room in rooms:
    if room.room_number == selected_number:
        if room.get_availability():
            room.set_availability(False)
            print(f"Great! Room {room.room_number} is now booked for you")
        else:
            print("Sorry, this room is unavailable more")
        break