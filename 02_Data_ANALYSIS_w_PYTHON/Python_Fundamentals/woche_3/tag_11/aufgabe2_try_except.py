# Miniaufgabe: Legt eine Exception für diesen Fall an.
# Die Ausgabe sollte im Fehlerfall.
# "Berlin ist aber keine Zahl lauten." bzw. entsprechend dem String-Value
val = "Berlin"
try:
    p = val / 1
except TypeError:
    print(f"{val} ist aber keine Zahl lauten.")
