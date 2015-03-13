dna =   ##insert DNA sequence

sdna = list(dna)

srna = []

for i in sdna:
    if i == "A":
        srna.append("A")
    if i == "C":
        srna.append("C")
    if i == "G":
        srna.append("G")
    if i == "T":
        srna.append("U")
        
        
rna = "".join(srna)
         
                    
print rna