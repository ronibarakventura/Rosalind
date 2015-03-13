dna =   ##insert DNA sequence

sdna = list(dna)

count_a = 0
count_c = 0
count_g = 0
count_t = 0

for i in sdna:
    if i == "A":
        count_a += 1
    if i == "C":
        count_c += 1
    if i == "G":
        count_g += 1
    if i == "T":
        count_t += 1
        
print count_a, count_c, count_g, count_t