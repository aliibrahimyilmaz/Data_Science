def get_float(x):
    return float(x)

def test(x):
    get_float(x)

try:
    test("x")
except TypeError as e:
    print(f"Log: email() an Administor: Fehler wurde aufgefangen {e}")