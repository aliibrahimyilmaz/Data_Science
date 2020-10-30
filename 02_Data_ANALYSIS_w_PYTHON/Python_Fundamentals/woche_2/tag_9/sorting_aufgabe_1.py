# Aufgabe: Sortiere die Zeichen in diesem String aufsteigend

my_str = "zoioczUuOcaeioAAaAieAAaBb"

chars = list(my_str)
chars = sorted(chars, key=lambda char: char.lower())
new_str = "".join(chars)
print(new_str)