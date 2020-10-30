"""1. Gegeben sind zwei Listen, füge diese zu einem Dictionary zusammen.
Iteriere über dieses Dictionary und gebe jeweils Kontinent -> Stadt aus
z.b  Europa => London"""
A = ['Europa', 'Asien', 'Afrika', 'Nord-Amerika', 'Süd-Amerika']
B = ['London', 'Hong Kong', 'Kapstadt', 'New York', 'Buenos Aires']
geo_dict = dict(zip(A, B))
print(geo_dict)

"""2. Schreibe eine Funktion get_city(), die einen Parameter besitzt.
Dieser Parameter soll als Key auf das Dictionary von 1) zugreifen und
den dazugehörigen Value ausgeben zb. get_city("Asien") ergibt "Hong Kong"""


def get_city(continent):
    return geo_dict[continent]


print(get_city("Asien"))

"""3. Schreibe eine Funktion swap(), die zwei Parameter besitzt und diese vertauscht zurückgibt
swap(1, 2) ergibt 2, 1"""


def swap(a, b):
    first = (b, a)
    str_list = []
    for i in first:
        str_list.append(str(i))
    result = ",".join(str_list)
    return result


print(swap(1, 2))

"""4. Lese die Temperaturen aus. Schreibe dazu eine Funktion get_temperature(),
 die den Ort entgegennimmt, und die Temperaturliste kommasepariert ausgibt
get_temperatures('berlin') ergibt 33, 42, 13, 11, 24, 22, 20, 10. """
temp = {
    "munich": [32, 22, 33, 11, 44, 12, 25, 15],
    "hamburg": [12, 22, 23, 11, 22, 12, 22, 8],
    "berlin": [33, 42, 13, 11, 24, 22, 20, 10]
}


def get_temperatures(stadt):
    tempstr_list = []
    for i in temp[stadt]:
        tempstr_list.append(str(i))
    result = ",".join(tempstr_list)
    return result


print(get_temperatures("berlin"))

"""4.1. Als Zusatz kann die Durchschnittstemperatur ausgegeben werden.
 Dies darf aber auf keinen Fall in der Funktino get_temperatures passieren,
sondern muss in einer anderen Funktion errechnet werden."""


def average_temp(stadt):
    temp_list = temp[stadt]
    return sum(temp_list) / len(temp_list)


print("die Durchschnittstemperatur ist: ", average_temp("berlin"))

"""5. Char-Counter. 
Schreibe eine Funktion char_counter(), die einen String entgegennimmt und
die einzelnen Zeichen des Strings zählt. Das Ergebnis soll ein Dictionary
mit den Vorkommen der Zeichen sein. Groß- und Kleinschreibung soll ignoriert werden.
Deutsche Umlaute werden umgeschrieben:
ä => ae
ü => ue
ö => oe
"""

deutsche_zeichen = {"ä": "ae", "ü": "ue", "ö": "oe"}


def alpha_convert(word):
    """umwandelt die bestimmten deutsche Zeichen in englische Zeichen"""
    converted_word = []
    for element in word:
        if element in ["ä", "ü", "ö"]:
            temp_list = list(deutsche_zeichen[element])
            converted_word.extend(temp_list)
        else:
            converted_word.append(element)
    return converted_word


def char_counter(word):
    """calculiert die Anzahl der einzelnen Zeichen des Strings"""
    output = word.lower()
    output = alpha_convert(output)
    counter = {}
    for element in output:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    return counter


result = char_counter("ÜöÄüÖä")
print(result)
