print('Enter DNA string')
a = str(input())
b = []
for i in range(len(a)):
    if a[i] == 'G':
        b.append('C')
    elif a[i] == 'C':
        b.append('G')
    elif a[i] == 'T':
        b.append('A')
    elif a[i] == 'A':
        b.append('U')
    else:
        print('INVALID OUTPUT')
        b.clear()
        break
print(str(''.join(b)))

