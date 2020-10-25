file = open("data.txt", "r")
content = file.read()[0:3]
print(content)
file.close()
