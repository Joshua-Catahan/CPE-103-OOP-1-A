fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

fhand= open('mbox-short.txt')
print(len(fhand.read()))

print(len(fhand.read()))