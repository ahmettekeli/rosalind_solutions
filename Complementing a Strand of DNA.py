def complementDna(dnaString):
    complementString = ''
    for i in dnaString:
        comp = ''
        if i == 'A':
            comp = 'T'
        elif i == 'T':
            comp = 'A'
        elif i == 'C':
            comp = 'G'
        else:
            comp = 'C'
        complementString = complementString + comp
    #returning reversed string    
    return complementString[::-1]
    
#let's see the result    
dnaSequence = 'TCCTGGGCGTCGTCTCTACTGAATAGAAACTGCACATACTAAAGTAGCCCCTGAACAGTCCAGAGTTCTTAGGCCTTGTTGCACTCCGCCGCGCGGCCACTTCGTCCTGAAGTTAGCTTTCCTGGCACACATACCAGAAAGATAAGTATCTTAAGGCTTATCGCTATCAACTCCGTTCCAATCAATGCGTGAGCAGAAGCACGAAGGCGGTCATGAGCCCTCCCGCTCACCACTCTTTTGTTGGAGCCAATATGTCACACAGGAGTAACTAGTAGTCGCGGGTTTGAACCGGTGACGCAAGACCCGCATTCTTACATTCGTCATTAACGTGTTGGGCTCGCTCAGAGATCGCACGGGTGCGCATGGTTAAGTAGGACACTCGAAAGGAACTGACCGACTACAACTGGTGAGCCCTCATAGCTCGCTTGAGTAAAACGTATGTGACTGTAGTCAAGTACGTACATCCTGTACTTGTAATTAAGGGCCCGTCATATACAGAACTTCCGGCTGTTACGTATGTCCTCTGGCTCTGTAGCTCGCGGTCAATCTTAATAACAAACGTACGTACGGATCGGCGACGCGTCCTGCCCTCCAGAACACGTGTATGTCAGCCTCGGAACATCATCCCGCACTTAAAAAAAGGACCTAAACCCCATTACGAACGGACCGACGGTGGACATAACATTACGGAATCTTTAAGCGAATCGATATCACAAGGTCTATGACACTCTCACGGGACCTACTTCTGAGTGAGTTCATTTATCACACTCCTGCATTGTCCTGGGCGCTTGTAGTGTGGTTGTGAGCAGTTTCAAAGGGCCATTCAGTGACCCGGAAACCGCCGAAAGGAAGCATGCAGTTCTTCCCGGCTGGCTATCAAAATCTCCCGCACTGG'
print(complementDna(dnaSequence))
    

