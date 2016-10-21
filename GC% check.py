
# Method without using biopyhon

f = open('/Users/kevin/Documents/Rosalind/rosalind_gc.txt', 'r')

max_ID, max_GC = '', 0

buf = f.readline().rstrip()  #rstrip is removing the '/n' at the end of each line
while buf:  # will keep looping while buf exists
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()  # keeps reading each newline as a new 'buf'
    while not buf.startswith('>') and buf:  # do this when a line without a '>' is found
        seq = seq + buf  # will concantate all lines together that belong to the same sequence
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G')) / float(len(seq))
    if seq_gc_content > max_GC:
        max_ID, max_GC = seq_name, seq_gc_content

print max_ID, '\n', max_GC*100
f.close()






#############################################################

# ...Or just use BIOPYTHON.
# then parse fasta file and calc GC% on each line.
from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq

maxGC = 0
for seq_record in SeqIO.parse('/Users/kevin/Documents/Rosalind/rosalind_gc.txt', 'fasta'):
    ID = seq_record.id
    newGC = GC(seq_record.seq)
    if newGC > maxGC:
        maxGC = newGC
        maxID = ID

#print maxID, round(maxGC, 7)  # if need to round
print maxID
print maxGC

    # so just use this, save the seq_record.id of each sequence, save the GC
    # % of each ID, then do the highest-GC%-check as I go through all of them.
    # then return the ID with the highest %GC




#################
# Failed attempts

# go through every other line in fasta file (even number lines), check if the ID is in
# the dictionary. If it isn't, add it and also add the line below it (the sequence)
# as the key for that ID. (Need to make a dictionary so I can pair all IDs and sequences together)

# Then check the %GC of the sequence. If the %GC is higher than the previous one
# (default set to 0), store this sequence & its ID as the highest %GC.

#####

# check every other (even numbered) line in string
#a = range(1,11)
#count = 0
#for i in range(1, len(a)+1):
#    count += 1
#    if count % 2 == 0:  # % does remainder-division. if remainder is 0, number is even. if remainder is 1, number is odd.
#        print i


# read every other line / IDs in file (odd numbered lines)
#count = 0
#for line in open('/users/kevin/desktop/test.txt', 'r'):
#    count += 1
#    if count % 2 == 1:
#        print line  # this is obv where the actual MEAT of the 'function' happens

# read each character
#maxGC2=0
#totalleng=0
#totalsum=0
#with open('/users/kevin/desktop/testfast.txt', 'r') as f:
#    for word in f:
#        if word.count(">") == 0:
#            leng = len(word)
#            totalleng = totalleng + leng
#            sum = word.count("G") + word.count("C")
#            totalsum = totalsum + sum
#            print totalsum
#        if word.count(">") == 1:
#            currGC = totalsum / totalleng
            #totalleng = 0
            #totalsum = 0
#            if currGC > maxGC2:
#                maxGC2 = currGC
#                maxID = currID
#            print word
        #print word
        #print word.count("G")
#        for ch in word:
#            if ch == '>':
                #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
