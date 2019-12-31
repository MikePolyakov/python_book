countries = {'Russia' : 'Europe', 'Germany' : 'Europe', 'Australia' : 'Australia'}

sqrs = {}
sqrs[1] = 1
sqrs[2] = 4
sqrs[10] = 100
print(sqrs)

myDict = dict([['key1', 'value1'], ('key2', 'value2')])
print(myDict)

phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
print(phones['police'])

phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
del phones['police']
print(phones)

phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
for service in phones:
    print(service, phones[service])

phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
for service, phone in phones.items():
    print(service, phone)

seq = map(int, input().split())
countDict = {}
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
for key in sorted(countDict):
    print(key, countDict[key], sep=' : ')

n = int(input())
latinEnglish = {}
for i in range(n):
    line = input()
    english = line[:line.find('-')].strip()
    latinsStr = line[line.find('-') + 1:].strip()
    latins = map(lambda s : s.strip(), latinsStr.split(','))
    for latin in latins:
        if latin not in latinEnglish:
            latinEnglish[latin] = []
        latinEnglish[latin].append(english)
print(len(latinEnglish))
for latin in sorted(latinEnglish):
    print(latin, '-', ', '.join(sorted(latinEnglish[latin])))