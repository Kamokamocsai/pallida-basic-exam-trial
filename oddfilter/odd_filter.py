# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

def odd_filter(numbers):
    temp = []
    for i in numbers:
        if i % 2 == 0:
            numbers.remove(i)
        elif i % 2 != 0:
            pass
    print(numbers)

print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]
