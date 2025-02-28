def smallest(numbers):
    smallest = 0
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest