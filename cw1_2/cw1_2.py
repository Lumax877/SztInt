import numpy as np


np.set_printoptions(suppress=True)
decision = np.loadtxt('dane/australian.txt')
decisionType = []
with open('dane/australian-type.txt') as file:
    for line in file:
        decisionType.append(line[-2])

rows, cols = decision.shape
print(rows,cols)
print(decisionType)

symbols = []
for i in decisionType:
    if i not in symbols:
        symbols.append(i)
print('Symbole klas decyzyjnych:', symbols)

TypeSize = []
for i in range(len(symbols)):
    TypeSize.append(0)

s_count = 0
n_count = 0
for i in decisionType:
    if i == 's':
        s_count +=1
    if i == 'n':
        n_count += 1

print('Wielkość klasy s =', s_count)
print('Wielkość klasy n =', n_count)

min = []
signmin = 100
for m in range(len(decisionType)):
    for n in range(0,rows-1):
        if decisionType[m] == 'n':
            if decision[n][m] < signmin:
                signmin = decision[n][m]
    min.append(signmin)
print('Minimalne wartości: ',min)

max = []
signmax = 0
for m in range(len(decisionType)):
    for n in range(0, rows-1):
        if decisionType[m] == 'n':
            if decision[n][m] > signmax:
                signmax = decision[n][m]
    max.append(signmax)
print('Maksymalne wartości: ',max)

unique = []
u_count = 0
for m in range(len(decisionType)):
    for n in range(0, rows-1):
        if decision[n][m] not in unique:
            unique.append(decision[n][m])
    print(unique)
    print(len(unique))
    unique = []

