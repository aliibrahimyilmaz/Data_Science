def summe(a: float, b: float) -> float:
    if a > 3:
        return a + b
    return None

summe(3, 3)  #mypy
print(summe.__annotations__)  # dunder attribute
# {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
# zahllose, endlose

