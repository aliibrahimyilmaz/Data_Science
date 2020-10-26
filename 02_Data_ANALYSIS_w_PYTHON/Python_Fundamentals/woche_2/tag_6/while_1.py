x = 0
y = 10
while x < y:
    x += 1
    print(x)

# erste Möglichkeit, while loop zu verlassen: break
while True:
    user_input = input("Bitte gebe eine Zahl ein: ")
    print(user_input)
    if user_input == "end":
        print("Goodbye")
        break

# zweite Möglichkeit, while loop zu verlassen: Bedingung
user_input = ''
while user_input != "end":
    user_input = input("Bitte gebe eine Zahl ein: ")
    print(user_input)

print("Hier gehts weiter")

# MAIN PROGRAM LOOP
# Schreibe einen Whileloop: der User kann ein Wort eingeben. Falls er eins der folgenden Wörter
# benutzt, bricht das Programm ab: close, exit, end

user_input = ''
while user_input not in ("end", "close", "exit"):
    user_input = input("Bitte gebe ein Wort ein: ")
    print(user_input)
print("Goodbye")


