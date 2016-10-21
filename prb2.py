import sys

f = file(sys.argv[1], 'r')
dna = f.read()

print dna.replace('T', 'U')
