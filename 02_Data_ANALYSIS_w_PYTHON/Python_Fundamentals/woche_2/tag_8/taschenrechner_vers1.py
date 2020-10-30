def summe(a, b):
    """Zwei Zahlen addieren, float oder int"""
    return a + b


def multiple(a, b):
    """Zwei Zahlen multiplizieren, float oder int"""
    return a * b


def division(a, b):
    """Zwei Zahlen dividieren, float oder int"""
    return a / b


def subtract(a, b):
    """Zwei Zahlen Substraction, float oder int"""
    return a - b


def get_user_input():
    """Userinput abfragen und diesen in nutzbare Bestandteile zerlegen"""
    eingabe = input("Bitte Operation eingeben(SUM, MULT, DIV, SUB), z.b SUM 2 4: ").split()
    operation = eingabe.pop(0)
    a, b = None, None
    if len(eingabe) >= 2:
        a = float(eingabe[0])
        b = float(eingabe[1])
    return operation, a, b


def print_result(result):
    """userfreundlicher Ausdruck des Ergebnises"""
    print("*" * 40)
    print(result)
    print("*" * 40)


OPERATIONS = {
    'sum': summe,
    'mult': multiple,
    'div': division,
    'sub': subtract
}


def controller(operation, a, b):
    """Die Ausführung der Operation"""

    if operation in OPERATIONS:
        op = OPERATIONS[operation]  # op ist Funktionreferenz
        result = op(a, b)  # Funktion aufrufen
        return result

    return "Operation not implemented"


while True:
    operation, a, b = get_user_input()

    if operation in ["quit", "end"]:
        break
    # Operation Ausführung
    result = controller(operation, a, b)
    # Ergebnis ausdrucken
    print_result(result)
