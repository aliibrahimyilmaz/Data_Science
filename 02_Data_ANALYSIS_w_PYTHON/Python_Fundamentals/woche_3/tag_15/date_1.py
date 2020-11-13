# Arbeiten mit Datum
# https://www.programiz.com/python-programming/datetime/strftime

from datetime import date, datetime
import locale

# Länderkennung
locale.setlocale(locale.LC_TIME, "de_DE")
# locale.setlocale(locale.LC_TIME, "tr_TR.utf8")

# aktuelle Datum
aktuelles_datum = date.today()
print(aktuelles_datum)  # YYYY-mm-dd  __repr__
print(type(aktuelles_datum))

# strftime formitiert das Datumsobjekt
euro_date = aktuelles_datum.strftime("%d-%m-%Y")
print(euro_date)
euro_date = aktuelles_datum.strftime("%A %d-%m-%Y")
print(euro_date)
weekday = aktuelles_datum.strftime("%A")
print(weekday)
monat = aktuelles_datum.strftime("%B")
print(monat)


# Datum definieren, d.h. Datumsobjekt erstellen
christmas2020 = date(2020, 12, 24)
print(christmas2020)
print(christmas2020.strftime("%d-%m-%Y"))
print(type(christmas2020.strftime("%d-%m-%Y")))

# Aktuelle Zeitpunkt
aktueller_zeitpunkt = datetime.now()
print("aktueller Zeitpunkt: ", aktueller_zeitpunkt)
print("aktueller Zeitpunkt: ", aktueller_zeitpunkt.strftime("%H:%M:%S"))

# Datetime Objekt erstellen
datum = datetime(2021, 5, 1, 12, 59, 0)
print("Monat des erstellen datetime Objekts: ", datum.strftime("%B"))

