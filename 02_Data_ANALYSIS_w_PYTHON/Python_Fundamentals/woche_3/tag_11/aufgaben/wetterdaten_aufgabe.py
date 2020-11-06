import re
data_file = 'wetterdaten.txt'

def get_data_dict(file_name:str)->dict:
    try:
        with open(file_name,"r", encoding="utf-8") as file:
            data = file.read()
        weeks = data.split("\n")
        print(weeks)
        weeks_list = list(map(lambda week: re.findall(r"\d\d", week), weeks))
        print(weeks_list)
        week_number_list = list(map(lambda week: week.pop(0), weeks_list))
        print(week_number_list)
        print(weeks_list)
        weeks_list = list(map(lambda week: list(map(int, week)), weeks_list))
        print(weeks_list)
        data_dict = dict(zip(week_number_list, weeks_list))
        return data_dict
    except:
        print("Dateiname stimmt nicht")
        return {}


print(get_data_dict(data_file))