from Models.room import Room, VIP_Room

rooms = [
    Room(101, "Single", 50, max_number_of_persons=1),
    Room(201, "Single", 50, max_number_of_persons=1),
    Room(301, "Single", 50, max_number_of_persons=1),
    Room(401, "Single", 50, max_number_of_persons=1),
    Room(102, "Standard Double", 80, max_number_of_persons=2),
    Room(202, "Standard Double", 80, max_number_of_persons=2),
    Room(302, "Standard Double", 80, max_number_of_persons=2),
    Room(402, "Standard Double", 80, max_number_of_persons=2),
    Room(103, "Triple", 110, max_number_of_persons=3),
    Room(203, "Triple", 110, max_number_of_persons=3),
    Room(303, "Triple", 110, max_number_of_persons=3),
    Room(403, "Triple", 110, max_number_of_persons=3),
    VIP_Room(501, 200, max_number_of_persons=8, has_free_breakfast=True),
    VIP_Room(502, 350, max_number_of_persons=12, has_free_breakfast=True)
]