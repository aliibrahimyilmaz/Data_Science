"""
print("Das ist das Name Abfrage Programm!")
user_input = input("Bitte gebe Deinen Namen ein: ")
print("das war die user eingabe: ", user_input)
print(type(user_input))
"""

''' 
print("Das ist das Zahl Abfrage Programm!")
user_input = int(input("Bitte gebe eine ganze Zahl ein: "))
print("das war die user eingabe: ", user_input)
print(type(user_input))
'''

'''Eine Fläche soll ermittelt werden. 
Der User gibt Länge und Breite in m in das Programm via input() ein und das 
Programm berechnet die Fläche. 
Die Ausgabe formatiert: Die Fläche beträgt 24 m2" '''

print("Das ist das Fläche Berechnung Programm!")
a = float(input("Bitte gebe eine Zahl für die Länge ein: "))
b = float(input("Bitte gebe eine Zahl für die Breite ein: "))
print("Die Fläche beträgt {} m2".format(a * b))
