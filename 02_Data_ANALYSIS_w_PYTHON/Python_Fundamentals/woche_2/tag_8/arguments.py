# Positionelle Parameter
def room(a, b, c):
    print("a:{} b:{} c:{}".format(a, b, c))


room(1, 2, 3)

# Keyword Argumente

def load_csv(file_name, encoding):
    print(file_name, encoding)


load_csv('aktienkurse.csv', "utf-8")  # Parameter
load_csv(encoding="utf-8", file_name='aktienkurse.csv')  # Argumente

# Posionelle Parameter und Keyword Argumente:

def control_sensor(a, b, flow, shutdown):
    print(a, b, flow, shutdown)

control_sensor(2, 2, shutdown=2, flow=0)
# control_sensor(shutdown=2, flow=0, 2, 2)  # SyntaxError: positional Argumente und Parameter follow keyword argument

# Unbestimmte Anzahl an positionellen Argumenten: *args

def summe(*args):  # args is ein Sequenz, Tuple
    print(sum(args))

summe(2, 3, 4, 5, 6, 7)


def summe(a, b, *args):  # Positionel und unbestimmte Anzahl der Argumenten
    print(sum(args))
    print(a+b)

    result = 0
    for x in args:
        result += x

    print("result: ", result)

summe(2, 3, 4, 5, 6, 7)

# Unbestimmte Anzahl an Keyword Argumenten: *kwargs

def username(**kwargs):
    print(type(kwargs))  # kwargs ist ein Dict.
    for k, v in kwargs.items():  # sehr hilfreich
        print("username: ", k, v)

username(name='B', last_name='C', age=33)


def username(*args, **kwargs):
    print(type(kwargs))  # kwargs ist ein Dict.
    print('kwargs', kwargs)
    print('args', args)
    for k, v in kwargs.items():  # sehr hilfreich
        print("username: ", k, v)

username(1, 2, 3, 4, name='B', last_name='C', age=33, encoding='utf-8')

# Default Parameter:

def calculate(a, b, save=False):
    print("calculate: ", a, b, save)
    if save:
        print("Speichere das Ergebnis")

calculate(2, 3)
calculate(2, 3, True)