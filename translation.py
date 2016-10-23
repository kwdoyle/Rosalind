# "nicer" way to more easily see what codons relate to each protein
codons = {}
codons = dict.fromkeys(['UUU', 'UUC'], 'F')
codons.update(dict.fromkeys(['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'L'))
codons.update(dict.fromkeys(['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'S'))
codons.update(dict.fromkeys(['UAU', 'UAC'], 'Y'))
codons.update(dict.fromkeys(['UAA', 'UAG', 'UGA'], 'Stop'))
codons.update(dict.fromkeys(['UGU', 'UGC'], 'C'))
codons.update(dict.fromkeys(['UGG'], 'W'))
codons.update(dict.fromkeys(['CCU', 'CCC', 'CCA', 'CCG'], 'P'))
codons.update(dict.fromkeys(['CAU', 'CAC'], 'H'))
codons.update(dict.fromkeys(['CAA', 'CAG'], 'Q'))
codons.update(dict.fromkeys(['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'R'))
codons.update(dict.fromkeys(['AUU', 'AUC', 'AUA'], 'I'))
codons.update(dict.fromkeys(['AUG'], 'M'))
codons.update(dict.fromkeys(['ACU', 'ACC', 'ACA', 'ACG'], 'T'))
codons.update(dict.fromkeys(['AAU', 'AAC'], 'N'))
codons.update(dict.fromkeys(['AAA', 'AAG'], 'K'))
codons.update(dict.fromkeys(['GUU', 'GUC', 'GUA', 'GUG'], 'V'))
codons.update(dict.fromkeys(['GCU', 'GCC', 'GCA', 'GCG'], 'A'))
codons.update(dict.fromkeys(['GAU', 'GAC'], 'D'))
codons.update(dict.fromkeys(['GAA', 'GAG'], 'E'))
codons.update(dict.fromkeys(['GGU', 'GGC', 'GGA', 'GGG'], 'G'))


with open('/Users/kevin/Documents/Rosalind/rosalind_prot.txt') as f:
    S = f.readline().rstrip()

cdn = ''
prt = ''
for i in range(0, len(S)):
    cdn += S[i]
    if len(cdn) == 3 and codons[cdn] != 'Stop':
        prt += codons[cdn]
        #if codons[cdn] == 'Stop':  # I guess this part is unnecessary due to adding != in the 1st if statement
        #    break
        cdn = ''


print prt



# go thru and add each amino acid into cdn. if len(cdn) == 3, then check what protein it corresponds to,
# save that protein in a new string, and then reset cdn.


# messier way to make the dict
#codons = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
#'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y',
#'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UCU':'C', 'UGC':'C',
#'UGA':'Stop', 'UGG':'W', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
#'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAA':'Q',
#'CAG':'Q', 'CGU':'R', 'CGC':'R', ''}



# Notes from solutions section: #

# this makes a 'messy' string full of spaces in between each character
string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

# basically removes the spaces and treats each 'word' as its own value (i.e., now table[0] will return 'UUU' instead of 'U' like string[0] would)
table = string.split()

transl8 = dict(zip(table[0::2], table[1::2]))

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))  # slicing via traL[start:end:step], with end blank

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print decoded
