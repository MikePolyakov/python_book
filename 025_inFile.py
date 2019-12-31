inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
for line in lines:
    print(line[-2::-1], file=outFile)
inFile.close()
outFile.close()

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    print(line[-2::-1], file=outFile)
inFile.close()
outFile.close()