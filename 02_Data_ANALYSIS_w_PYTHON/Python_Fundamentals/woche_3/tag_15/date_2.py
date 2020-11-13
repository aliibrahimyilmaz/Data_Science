from datetime import datetime

t2 = "19 1 12"  # exotische Datumsformat: Jahr Monat Tag
d = datetime.strptime(t2, "%y %m %d")
print(d)

t1 = "2019-12-24 18:00:00"
d = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
print(d)
print(type(d))
