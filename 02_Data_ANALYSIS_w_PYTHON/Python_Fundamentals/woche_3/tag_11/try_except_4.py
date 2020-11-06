def get_float(x):
    return float(x)


def my_test(x):
    get_float(x)


try:
    my_test("x")
except TypeError as e:
    print(f"Log: email() an Administor: Fehler wurde aufgefangen {e}")
except ValueError as e:
    print("Fehler")