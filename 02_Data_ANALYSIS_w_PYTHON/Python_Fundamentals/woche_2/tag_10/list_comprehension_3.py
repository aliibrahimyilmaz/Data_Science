# Mehrere for Loopen
cart_product = [(a, b) for a in [1, 2] for b in [2, 4]]  # wie Nested_loop
print(cart_product)

# herkömmliche Schreibweise:
cart_product = []
for a in [1, 2]:
    for b in [2, 4]:
        cart_product.append((a, b))
print(cart_product)

# SET Comprehension (Mengen Abstraktion)
cart_product = {(a, b) for a in [1, 2] for b in [2, 4]}
print(cart_product)

# french cards: king, queen, ace, jack
french_deck = [(a, b) for a in ["♠", "♥", "♣", "♦"] for b in ["K", "Q", "A", "J"]]
print(french_deck)

french_deck = [(a, b)
               for a in ["♠", "♥", "♣", "♦"]
               for b in ["K", "Q", "A", "J"]
               ]
print(french_deck)