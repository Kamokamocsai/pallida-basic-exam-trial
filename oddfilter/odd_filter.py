def odd_filter(numbers):
    temp = []
    for i in numbers:
        if i % 2 == 0:
            numbers.remove(i)
        elif i % 2 != 0:
            pass
    print(numbers)

print(odd_filter([1, 2, 3, 4, 5]))
