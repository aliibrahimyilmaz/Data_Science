my_liste = [(1, 2), (1, 1), (0, 2)]
new_list = [(1, 2), (1, 1)]
counter = 0
for i in new_list:
    if i in my_liste:
        counter += 1

print(counter)

for x in range(3):
    print(x)