# Aufgabe: erstelle eine Funktion, die als Parameter eine Liste erwartet und
# jeweils den ersten Buchstabens eines Elements in Uppercase wandelt.
# z.b eggs => Eggs spam whomp = Spam Whomp
# Return Liste

monty = ['eggs', 'spam whomp', 'cheese', 'ham']


def my_title(your_list):
    # return [i.title() for i in your_list]  # oder
    return list(map(lambda s: s.title(), your_list))


print(my_title(monty))
