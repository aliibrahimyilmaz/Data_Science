a = 3
if a > 3:
    b = 2
else:
    b = 4

# Ternäre Operator
b = 2 if a > 3 else 4

# ternary Operator
A = [True if a % 2 == 0 else False for a in range(10) if a >= 5]
print(A)


# Herkömmliche Version
A = []
for a in range(0, 10):
    if a >= 5:
        A.append(True if a % 2 == 0 else False)
print(A)