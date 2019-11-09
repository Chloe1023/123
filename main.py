a = [ 3, 2, 1, 4, 5 ]
for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j-1] > a[j]:
            w = a[j]
            a[j] = a[j-1]
            a[j-1] = w

for i in range(len(a)):
    print(a[i], end="")
