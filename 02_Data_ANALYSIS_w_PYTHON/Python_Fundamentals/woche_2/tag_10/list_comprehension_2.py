a = ["AAA", "BBB"]
for x in a:
    print(x)

res = [print(x) for x in a]
print(res)

# Mapping mit List Comprehension: Bevorzugte Weg
[print(x) for x in a]

b = [(x, x**2) for x in [1, 2, 3, 4]]
print(b)  # List-Tuple

c = [[x, x**2] for x in [1, 2, 3, 4]]
print(c)  # List-List

d = [(lambda x: [x, x**2])(x) for x in [1, 2, 3, 4]]
print(d)  # Lambda List-List
