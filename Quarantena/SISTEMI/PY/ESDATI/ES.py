def adj2dict(m):
    d = {}
    for n in range(0,len(m)):
        d[n] = m[n]
    return d

from sys import argv

dati = open(argv[1], 'r')
lines = dati.readlines()

matrix = []

for line in lines:
    #code
    column = [False for k in range(0,len(lines))]
    numbers = line.split(' ')
    patient = int(numbers[0])
    numbers.pop(0)
    spreaded = [int(i) for i in numbers]
    for s in spreaded:
        column[s] = 1
    matrix.append(column) 

for k,v in adj2dict(matrix).items():
    print(f'{k} : {v}')
        
dati.close()