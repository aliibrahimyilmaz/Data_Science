def hello_world():
    print("Hello World!")

x = hello_world()
print(x)  # Default Rückgabewert von print() ist None.

x = print("test")
print(x)

def my_print():
    print("das ist meine Print Funktion")

my_print()

def say_hello(first_name,last_name):  # zwei parameter
    print(f"{first_name} {last_name} sagt Hallo!")

say_hello("Ali", "Yilmaz")
say_hello("Julian", "Menges")
say_hello("Saber", "Darabi")

def raum_inhalt(a, b, c):
    return a * b * c

volume = raum_inhalt(3, 4, 5)
print(f"raum_inhalt is {volume}")

# Grad Celcius an die Funktion übergeben, und als Rückgabewert Grad Fahrenayt erhalten
def grad_convert(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius} celcius ist {fahrenheit} fahrenheit.")

grad_convert(100)
