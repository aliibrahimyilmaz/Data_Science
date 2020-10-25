string = "das ist ein String"
print(string)
print(type(string))

# Zeichen an Index 0
print(string[0])  # index 0

# Aufgabe Index 4:
print("Index 4: ", string[4])  # index 4

# Fehler: Index out of Range
#print(string[100])

# Aufgabe: letztes Zeichen eines Strings mit negativem Index
print("Letztes Zeichen: ", string[-1])

# string = 'It's ok''  # Fehler!
string = "it's ok"

# addieren, concatenate
a = "AAA"
b = "BBB"
c = a + b  # Operatoren Überladung
print(c)
d = a + " " + b
print(d)

# String wiederholen
string = "*"
print(string * 100)  # Operatorenüberladung
#oder
sternchen = string * 100
print(sternchen)

# string = "Schulnote: " + 3 # Fehler
string = "Schulnote: " + str(3)
print(string)

b = "San Francisco"
print(len(b))









