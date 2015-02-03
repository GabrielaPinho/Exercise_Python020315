# Processing DNA in a file

file = open("input.txt")
my_file = open ("sequences.txt", "w")
for line in file:
    seq = line[14:]
    my_file.write(seq)
my_file.close()


