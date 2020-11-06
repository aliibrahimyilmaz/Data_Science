# große Listen sollten nicht mit List Comprehension erstellt
euc = [(x, y, z) for x in range(0, 100) for y in range(0, 100) for z in range(0, 100)]
#print(euc)
#print(euc[3])

print("*"*40)
# lazy (Generator Expression)
b = 3
print(globals())


euc = ((x, y, z) for x in range(0, 10) for y in range(0, 10) for z in range(0, 10))
# print(euc)
# print(euc[3]) Fehler! 'generator' objekt is not subscriptable
b = 5
print(globals())


print("*"*40)

# Iterieren über Generator Objekt
# for t in euc:
    # print(t)

# print(globals())




