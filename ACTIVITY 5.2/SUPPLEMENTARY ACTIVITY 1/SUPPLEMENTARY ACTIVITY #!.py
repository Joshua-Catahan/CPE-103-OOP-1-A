# Write analysis to SURNAME.txt
with open("CATAHAN.txt", "w") as fhand:
    fhand.write("Line 1: This file demonstrates file operations in Python.\n")
    fhand.write("Line 2: We can create, read, update, and delete files.\n")

# Read and print contents
with open("CATAHAN.txt", "r") as fhand:
    for line in fhand:
        print(line.strip())
