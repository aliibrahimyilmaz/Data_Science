# https://www.w3schools.com/python/python_ref_dictionary.asp
population = {
'Berlin': 3748148,
'Hamburg': 1822445,
'München': 1471508,
'Cologne': 1085664,
}
# Einfügen:
population['Dortmund'] = 600000
print(population)

# element aus dem Dict löschen
del population['Berlin']
print(population)

population.clear()
print(population)