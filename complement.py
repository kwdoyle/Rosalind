import sys
from Bio.Seq import Seq

f = file(sys.argv[1], 'r')
dna = f.read()

dna2 = Seq(dna)
print dna2.reverse_complement()
