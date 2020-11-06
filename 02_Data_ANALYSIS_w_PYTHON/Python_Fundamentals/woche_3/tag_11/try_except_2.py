try:
    with open("gibtsnicht.txt") as file_handler:
        content = file_handler.read()
except FileNotFoundError:
    content = None

print(content)

# user_input, den wir als Ganzzahl benötigen. Mit int konvertieren
user_input = "0,3"
try:
    print(int(user_input))
except ValueError:
    print("Umwandlung hat nicht funktioniert")

# ValueError
try:
    a = float("0.01")
except ValueError:
    a = 0
print(a)
