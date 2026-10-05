class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = self.generate_id()

    def generate_id(self):
        return self.firstname[:3].lower() + self.lastname[:3].lower() + "_id" # TODO: generate unique id

    def __str__(self):
        return f"{self.firstname} {self.lastname}"