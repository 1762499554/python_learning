# coding=utf-8

import sys
from itertools import permutations

def check(list):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            return False
    return True
ssn = []
while True:
    sn = input().strip()

    if sn == '':
        break
    sn = list(sn.split())
    ssn.append(sn)

number = int(ssn[0][0])
aa = []
for i in range(number+1):
    aa.append(i)
aa.remove(aa[0])
arrangement = list(permutations(aa))

K = 0
result = []
for iterable in arrangement:
    K = 0
    cc = list(iterable)

    if check(cc)==True:
        K = 0
        result.append(K)
        continue
    else:
        for i in range(number):
            if check(cc) == True:
                result.append(K)
                break
            for j in range(0, number-i-1):
                if cc[j] > cc[j + 1]:
                    cc[j], cc[j + 1] = cc[j + 1], cc[j]

            K += 1
wordfreq = []

for w in result:
    wordfreq.append(result.count(w))

d = dict(zip(result,wordfreq))
print(d)
for i in d.values():
    print(str(i)+'\n')







