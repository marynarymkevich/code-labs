class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def generate_id(self):
        self.id = self.firstnamer[:3] + self.lastname[:3] + "_id" # TODO: generate unique id

    def __str__(self):
        return f"{self.firstname} {self.lastname}"