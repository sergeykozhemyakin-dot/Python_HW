class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand,
        self.model = model,
        self.phone_number = str(phone_number)

    def __str__(self):
        return f"Smartphone({self.brand}, {self.model}, {self.phone_number})"

    def __repr__(self):
        return self.__str__()