def square(x):
    return x ** 2

# user_defined function
numbers = [1, 2, 3]
numbers = map(square, numbers)  # <map object at 0x000002976BF58E48>
numbers = list(numbers)
print(numbers)

# lambda function
numbers_2 = [4, 5, 6]
numbers_2 = map(lambda x: x ** 2, numbers_2)  # mit lambda geht das auch
numbers_2 = list(numbers_2)
print(numbers_2)

# list comprehension
numbers_3 = [7, 8, 9]
numbers_3 = [x ** 2 for x in numbers_3]  # bevorzugt erst.
print(numbers_3)



