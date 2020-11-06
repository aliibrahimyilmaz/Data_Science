weekday_temperatures = [
{'day': 'Monday',    'date': '2019-07-15', 'temperature': 31},
{'day': 'Tuesday',   'date': '2019-07-16', 'temperature': 33},
{'day': 'Wednesday', 'date': '2019-07-17', 'temperature': 27},
{'day': 'Thursday',  'date': '2019-07-18', 'temperature': 25},
{'day': 'Friday',    'date': '2019-07-19', 'temperature': 30},
{'day': 'Saturday',  'date': '2019-07-20', 'temperature': 31},
{'day': 'Sunday',    'date': '2019-07-21', 'temperature': 29},
{'day': 'Monday',    'date': '2019-07-22', 'temperature': 25},
{'day': 'Tuesday',   'date': '2019-07-23', 'temperature': 31},
{'day': 'Wednesday', 'date': '2019-07-24', 'temperature': 26},
{'day': 'Thursday',  'date': '2019-07-25', 'temperature': 23},
{'day': 'Friday',    'date': '2019-07-26', 'temperature': 22},
{'day': 'Saturday',  'date': '2019-07-27', 'temperature': 23},
{'day': 'Sunday',    'date': '2019-07-28', 'temperature': 32}
]

weekends = ["Saturday", "Sunday"]

def get_hot_work_days():
    return [(weekday["date"], weekday["temperature"]) for weekday in weekday_temperatures
                     if weekday["day"] not in weekends and weekday["temperature"] >= 30]

print(get_hot_work_days())
