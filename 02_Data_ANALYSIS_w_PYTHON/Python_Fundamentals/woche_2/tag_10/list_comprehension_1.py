personen = ["Bernd", "Klaus", "Peter", "Claudia", "Petra", "Otto", "Walter", "Benjamin"]
new_persons = []

new_persons = [name for name in personen if name.startswith('B')]
print(new_persons)

# übungsaufabe: filtere alle Zahlen aus der Liste, die durch 2 teilbar sind
liste = [1, 2, 3, 4, 9, 11, 24, 10, 7]

# a) auf herkömmlichen Weg:
num_list = []
for num in liste:
    if num % 2 == 0:
        num_list.append(num)
print("herkömmlich: ", num_list)

# b) als List Comprehension:
evens = [num for num in liste if num % 2 == 0]
print("List Comprehension: ", evens)

gros_evens_1 = [num for num in liste if num % 2 == 0 and num > 6]
print("List Comprehension: ", gros_evens_1)

gros_evens_2 = [num for num in liste if num % 2 == 0 if num > 6]
print("List Comprehension: ", gros_evens_2)