from __future__ import division

with open('/users/kevin/Documents/Rosalind/rosalind_iprb.txt') as f:
    for line in f:
        data = map(int, line.split())  # map here is making everything in the given line into an integer

AA = data[0]
Aa = data[1]
aa = data[2]
total = AA + Aa + aa

# calculate P(having at least 1 dominant)
pAAxAA = AA/total * (AA-1)/(total-1)
pAAxAa = AA/total * Aa/(total-1)
pAAxaa = AA/total * aa/(total-1)

pAaxAa = Aa/total * (Aa-1)/(total-1) * 3/4
pAaxAA = Aa/total * AA/(total-1)
pAaxaa = Aa/total * aa/(total-1) * 1/2

#paaxaa = aa/total * (aa-1)/(total-1)
paaxAa = aa/total * Aa/(total-1) * 1/2
paaxAA = aa/total * AA/(total-1)

print sum([pAAxAA, pAAxAa, pAAxaa, pAaxAa, pAaxAA, pAaxaa, paaxAa, paaxAA])



# calculate 1 - P(having all recessive)
pAaxAa = Aa/total * (Aa-1)/(total-1) * 1/4
pAaxaa = Aa/total * aa/(total-1) * 1/2
paaxAa = aa/total * Aa/(total-1) * 1/2  # you have to account for the prob of the reverse maiting pair.
paaxaa = aa/total * (aa-1)/(total-1)


print 1-sum([pAaxAa, pAaxaa, paaxAa, paaxaa])
