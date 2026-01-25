def month_to_season():
    number_of_month=int(input("Введите номер месяца от 1 до 12:"))
    if number_of_month == 12 or number_of_month in range (1, 3):
        print("Зима")
    elif number_of_month in range (3, 6):
        print("Весна")
    elif number_of_month in range (6,9):
        print("Лето")
    elif number_of_month in range (9, 12):
        print ("Осень")

month_to_season()
