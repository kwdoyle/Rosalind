# "normal" way

with open('/users/kevin/downloads/rosalind_hamm.txt', 'r') as f:
    data = f.readlines()
count = 0
for i in range(0, len(data[0])):
    if data[0][i] != data[1][i]:
        count += 1
print count


# "faster" way
zoup = zip(data[0], data[1])  # can zip things to make tuple pairs of each character in two lines of a string
cournt = 0
for i in range(0, len(zoup)):
    if zoup[i][0] != zoup[i][1]:
        cournt += 1
print cournt


# faster way to do the above
print sum([i != j for i, j in zip(data[0], data[1])])
