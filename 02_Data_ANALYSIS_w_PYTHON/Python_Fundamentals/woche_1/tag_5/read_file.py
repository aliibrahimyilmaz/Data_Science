file = open("data2.txt", "r", encoding="utf-8")
content = file.read()
#print(content)
file.close()

# Dateien öffnen mit with Kontext-Manager, es wird automatisch geschlossen.
with open("data2.txt", "r", encoding="utf-8") as file:  # default is read-mode
    # lesen wir die gesamt ein
    content2 = file.read()  # ergebnis ist ein string
    #print('a', content2)

with open("data2.txt", "r", encoding="utf-8") as file:  # default is read-mode
    # lesen wir die gesamt ein
    content3 = file.readlines()  # ergebnis ist eine Liste
    #print(content3)

with open("data2.txt", "r", encoding="utf-8") as file:  # default is read-mode
    # lesen wir die gesamt ein
    for line in file:
        print('zeile', line)

