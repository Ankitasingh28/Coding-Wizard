palin_num = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        x = a * b
        if x > palin_num:
            s = str(a * b)
            if s == s[::-1]:
                palin_num = a * b
print(palin_num)