a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]


def list_parse(value: list) -> tuple:
    error_list = []
    b = []
    for element in value:
        try:
            b.append(float(element))
        except ValueError as e:
            if "," in element:
                element_new = element.replace(",", "")
                if element_new.isdigit():
                    b.append(float(element.replace(",", ".")))
                else:
                    error_list.append(element)
            else:
                error_list.append(element)
    return b, error_list


float_list, err_list = list_parse(a)
print(float_list, err_list)
