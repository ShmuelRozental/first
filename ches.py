for i in range(1, 9):
    row = []

    for j in range(1, 9):
        if i+j % 2 == 0:
            row.append("black")
        else:
            row.append("white")
    print(row)





a = [0, 1, 1, 1, 1, 0, 0, 0, 0]
zerozugy = 0
zeropered = 0
onezugy = 0
onepered = 0
for i in range(len(a)):
    print(i)
    if a[i] == 0:
        if (a[i] + i) % 2 == 0:
            zerozugy += 1
        else:
            zeropered += 1

    else:
        if (a[i] + i) % 2 == 0:
            onezugy += 1
        else:
            onepered += 1


print(zerozugy, zeropered , onezugy, onepered)