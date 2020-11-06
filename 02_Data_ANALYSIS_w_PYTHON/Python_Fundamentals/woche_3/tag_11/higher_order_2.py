words = ["quux", "bar", "grumpy", "barfoo", "waldo"]  # metasyntaktischen Variablen
# Die erste heisst foo, die zweite bar

def fn(x):
    """x ist Element der Sequenz"""
    # return len(x) > 5
    if len(x) > 5:
        return True
    return False

long_words = filter(fn, words)
print(long_words)  # filter Objekt, ist ein Iterator- list() verwenden, um daraus eine Liste zu machen
print([i for i in long_words])


# Aufgabe: Umschreiben als List Comprehension
long_words = [word for word in words if len(word) > 5]
print(long_words)

long_words_generator = (word for word in words if len(word) > 5)  # mit runde clammen: generator
print(long_words_generator)
print([i for i in long_words_generator])
