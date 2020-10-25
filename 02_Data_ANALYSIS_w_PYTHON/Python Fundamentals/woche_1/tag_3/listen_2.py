from copy import deepcopy  # oder "import copy" dann "copy.deepcopy"

# verschachtelte Listen kopien
cars = ["Audi", "Porsche"]
cars2 = deepcopy(cars)  # cars2 hat total andere Referenz
print(id(cars))
print(id(cars2))
print(cars2)
cars.append("Mercedes")
print(cars2)
print(cars)