from datetime import date, datetime

heute = datetime.today()
geburtstag = datetime(1983, 10, 4)

alter = heute - geburtstag
print(type(alter))
print(dir(alter))
print(alter/365)
print(alter)