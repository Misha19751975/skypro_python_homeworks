class Address:
    def __init__(self, index, citi, street, house, appt):
        self.index = index
        self.citi = citi
        self.street = street
        self.house = house
        self.appt = appt

    def __str__(self):
        return f"{self.index}, {self.citi}, {self.street}, {self.house}, {self.appt}"
        

    