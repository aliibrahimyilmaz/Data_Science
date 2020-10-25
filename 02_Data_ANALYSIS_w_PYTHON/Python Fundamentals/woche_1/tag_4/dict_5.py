from pprint import pprint
# element counting in a list und in der Liste ausgeben
a = ["a", "b", "c", "a", "c", "d", "a"]
counter = {}
for element in a:
    if element in counter:
        counter[element] = counter[element] + 1
    else:
        counter[element] = 1
pprint(counter, width= 1)
print(counter)
