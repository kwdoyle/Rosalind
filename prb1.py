f = open('rosalind_dna.txt', 'r')
dna = f.read()

for i in 'ACGT':
    print dna.count(i),
