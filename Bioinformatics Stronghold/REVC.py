dna = ##insert DNA sequence

sdna = list(dna)

ldna = []

for i in sdna:
    if i == "A":
        ldna.append("T")
    if i == "C":
        ldna.append("G")
    if i == "G":
        ldna.append("C")
    if i == "T":
        ldna.append("A")
        

p = len(ldna)
cdna = ldna[p::-1]
revcdna = "".join(cdna)
         
                    
print revcdna