# Multiple exons from genomic DNA

exon_position = open("exons.txt")
genomic = open ("genomic_dna.txt")
sequence = genomic.read()
document = open("Coding_seq.txt", "w")
coding = ""
for line in exon_position:
    position = line.split(",")
    start = int (position[0])
    final = int (position[1])
    exon = sequence[start:final]
    coding = coding + exon
document.write(coding)
document.close()
