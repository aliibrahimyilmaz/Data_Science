# das Error Objekt

try:
    p = 4 / 0
except (ZeroDivisionError, ValueError) as e:
    print("e: ", e)
    print("type: ", type(e))
    print("dir: ", dir(e))
    print("doc: ", e.__doc__)  # Doc String: Second argument to a division or modulo operation was zero.
    print("args: ", e.args)
    print("traceback: ", e.__traceback__)

