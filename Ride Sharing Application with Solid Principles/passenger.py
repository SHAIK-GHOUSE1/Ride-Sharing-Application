from user import User

class Passenger(User):
    def __init__(self, name, email, location):
        super().__init__(name, email, location)