string = "Teststring"
print("erst index: ", string[0])

x = string[0:2]
print("x: ", x)

x = string[1:3]
print("x 1-3: ", x)

x = string[2:]
print("x 2:bis ende: ", x)

x = string[:]
print("x komplett: ", x)

x = string[:-1]
print("x komplett: ", x)

x = string[:38]
print("x komplett: ", x)

# Übung
# Schneide jeweils alle B aus den Strings
x = "AAAAB"
print(x[:-1])  # => AAAA
y = "BBAAABBB"
print(y[2:5])  # => AAA
z = "AAAABBBB"
print(z[:4])  # => AAAA
t = "ABBBBB"
print(t[0])  # => A
k = "BBA"
print(k[-1])  # => A

string = "Teststring"
x = string[-2:]
print("x letzte zwei: ", x)

string = "Teststring"
x = string[-2:-1]
print("x letzten zweite: ", x)

# ABABAB
# [start:stop:step]
numbers = "123456789"
odds = numbers[::2]  # ungerade Zahlen
print(odds)
evens = numbers[1::2]  # gerade Zahlen
print(evens)

numbers = numbers[::-1]
print("umgedreht: ", numbers)

print(numbers[6], numbers[3])