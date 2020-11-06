def dispatch(x: bool = True) -> None:
    print(x)

# int float list dict string bool byte bytearray
def filter_fruits(fruits: list, char: str) -> list:
    """return gefilterte Liste"""
    return fruits

# Function Annotations:
def set_control(*args: "collection of arguments"):
    pass

print(set_control.__annotations__)  # {'args': 'collection of arguments'}

liste = [
    "A",
    "B",
    "C"
]
d = {
    "d": 2,
    "x": 33,
}

import typing  # Module Typing
# https://realpython.com/python-type-checking