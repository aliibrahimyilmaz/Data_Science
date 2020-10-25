# Strings verketten, einfachste Methode (schlechteste Methode)
str1 = "Baum"
str2 = "haus"
str3 = str1 + str2
print(str3)

# besser ist die format-Methode()

# String-Methode format() und Platzhalter
string1 = "Vorname: {}, Nachname: {}"
string1 = string1.format("Michael", "Meier")
print(string1)

# übergebene Werte können auch Zahlen sein
string1 = "Berlin: {}, Hamburg: {}, München: {}".format(2, 4, 1/3)
print(string1)

string1 = "a: {} b: {} c: {}".format(1, 2, 3)
print(string1)
string1 = "a: {2} b: {0} c: {1}".format(4, 6, 9)
print(string1)

# Float Value formatieren mit format() und Formatvorgabe
string1 = "Berlin: {}, Hamburg: {}, München: {:.2f}".format(2, 4, 1/3)
print(string1)

# gleichen Wert in Platzhalter mit selbem Index schreiben
string1 = "precision: {0:.2f} or {0:.1f}".format(331.4148)
print(string1)

string1 = "gleicher Index: {0} or {0}".format(331.4148)
print(string1)

ad = "Vorname: {}, Nachname: {}, Strasse: {}, PLZ: {}, Ort: {}, Bundesland: {}".format(
    "Peter",
    "Keller",
    "Stadtweg 3",
    "93893",
    "Berlin",
    "city"
)
print(ad)

# f-string method
f = f"a:{4.34:.1f}, b:{'Berlin'}, c:{1/3:.3f}"
print(f)




