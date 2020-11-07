import time


status_current = 0
h = 0
num=0
def NonRecursiveCollatz(i):
    counter = 1
    while i != 1:
        counter = counter + 1
        if i%2 == 0:
            i = i / 2
        else:
            i = 3*i + 1
    return counter
time_start = time.time()
for i in range(1,1000000):
    status_current = NonRecursiveCollatz(i)
if status_current > h:
    h = status_current
    num = i


run_time = time.time() - time_start

print("Highest chain")
print(h)
print("From number ")
print(num)
print("Time taken " )
print(run_time)