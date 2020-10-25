import time
n= 100000
start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)

n= 100000
start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)

# append ist schneller als + Operator
n= 100000
start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)