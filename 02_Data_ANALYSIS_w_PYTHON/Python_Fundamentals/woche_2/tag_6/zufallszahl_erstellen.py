# 2. Zufallszahl erstellen
# Schreibe eine Funktion generate_number(), die eine Zufallszahl in einem definierten
# Wertebereich erstellt.
# generate_number() erwartet zwei Parameter: minimum für das Minimum, und maximum für das Maximum.
# Beispiel
# random_number = generate_number(3, 10)
# // 8

import random
def generate_number(mini, maxi):
    return random.randint(mini, maxi)

random_number = generate_number(3, 10)
print(random_number)