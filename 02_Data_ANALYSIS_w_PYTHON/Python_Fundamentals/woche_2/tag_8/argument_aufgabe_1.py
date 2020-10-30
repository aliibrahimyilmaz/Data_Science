# Aufgabe. Schreibe eine Funktion filter_address mit **kwargs
# Der Funktion werden name, last_name und street übergeben.
# Falls die Straße mit einem großen T beginnt, soll der Wert von street auf None gesetzt werden.
# return dict

def filter_address(**kwargs):
    if kwargs["street"][0] == "T":
        kwargs["street"] = None
    return kwargs

address_dict = filter_address(name='Python', last_name='Anaconda', street='Tuple Str 5', city='Alfacity')
print(address_dict)

