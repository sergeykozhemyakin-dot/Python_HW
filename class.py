class User:
    def __init__(self, name):
        print(f"Я создался,меня зовут {name}")
        self.name = name


    def addName(self, date):
        self.date = date
        date = input("Введите дату регистрации:")
        print(f"Вы в сети {date} лет")

    def Card(self):
        card_number = "1234-5678-1234-5678"
        self.card = card_number
        print(f"Номер карты: {card_number}")


max = User("Max")
max.addDate()