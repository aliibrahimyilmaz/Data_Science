from functools import reduce

# mit Lambda
numbers = [1, 2, 3, 4]  # sum(numbers)
summe = reduce(lambda x, y: x + y, numbers)
print(summe)

# mit def:

def my_sum(x, y):
    print("x: ", x, "y: ", y)
    return x + y

numbers = [1, 2, 3, 4]  # sum(numbers), products(numbers)
summe = reduce(my_sum, numbers)
print(summe)

def p(x, y):
    return x * y

def product(seq):
    return reduce(p, seq, 10)  # 10 ist initial value: Initialwert

produkt = product(numbers)
print(produkt)

minimum = reduce(lambda x, y: x if x < y else y, numbers)  # minimum number in a list
print(minimum)

mini = min(numbers)
print(mini)

