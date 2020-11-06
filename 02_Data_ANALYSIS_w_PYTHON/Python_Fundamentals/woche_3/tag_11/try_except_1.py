# https://docs.python.org/3/library/exceptions.html
user_input = 0
x = 0
try:
    x, a = 0, "Test"
    x = 3 / "something"  # Type_Fehler
    x = 3 / user_input # ZeroDivisionError
    b = "Test"
except ZeroDivisionError:
    print("das ist schiefgegangen")
except TypeError:
    print("hier ist ein Type_Fehler aufgetreten")

print("x: ", x)
print("a: ", a)
# print("b: ", b)  # geht nicht, da b nicht definiert

