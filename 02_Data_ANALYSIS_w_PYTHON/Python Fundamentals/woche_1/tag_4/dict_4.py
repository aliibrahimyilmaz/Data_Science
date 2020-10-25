population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}
# population['Berlin'] = 1
# population['München'] = 1
# Dict-Methode update, um ein Dictionary upzudaten
population.update(
    {'Berlin': 1,
     'München': 2,
     },
)
print(population)