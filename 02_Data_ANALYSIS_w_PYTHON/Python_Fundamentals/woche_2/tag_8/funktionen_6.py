def p():
    print("test")


print(type(p))
print(id(p))
print("Funktionsreferenz", p)
p()

# Variable a wird auf p referenziert
a = p  # umkopieren

print(type(a))
print(id(a))
a()

# Wir weisen myprint auf Funktionen
myprint = print
myprint("hallo")

func_liste = [a, p]
for func in func_liste:
    print(func)

