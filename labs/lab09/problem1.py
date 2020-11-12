def counter():
    numbers_sum = 0.0
    squares_sum = 0.0
    count = 0
    while True:
        number = yield
        count += 1
        numbers_sum += number
        squares_sum += number ** 2

        average = numbers_sum / count
        average_square = squares_sum / count
        print(f"{count} numbers entered, average is {average}, std is {average_square - average ** 2}")


coroutine = counter()
next(coroutine)
for i in range(5):
    number = float(input())
    coroutine.send(number)

