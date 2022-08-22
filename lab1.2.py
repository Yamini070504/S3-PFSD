class Passenger:
    +
    def __init__(self, name, verification_id):
        self.name = name
        self.verification_id = verification_id
class Coach(Passenger):
    def __init__(self, type, number):
        self.type = type
        self.number = number
tickets = 60
while tickets!=0:
    passenger = Passenger()
    print("Successfully booked")
else:
    print("Not enough tickets")+