"""my_list = [(2, 5), (2, 6), (2, 7)]

my_list.index((2, 7))
print(my_list.index((2, 7)))

board = []

#Create a 5x5 2 dimensional list
for x in range(10):
    board.append(["O"] * 10)

print(board)"""
import pandas as pd
x = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
operation_area = pd.DataFrame(data=x, columns=columns, index=index)
print(operation_area)
operation_area[1][2] = "S"
operation_area.loc[1, 1] = "X"
print(operation_area)