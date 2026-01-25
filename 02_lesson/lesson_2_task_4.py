def fizz_buzz():
    n = int(input("Введите число:"))
    for numbers in range(1, n):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 5 == 0:
                print("Buzz")
        elif numbers % 3 == 0 :
                print("Fizz")
        else:
            print(numbers)

fizz_buzz()
