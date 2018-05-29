# -*- coding: utf-8 -*-

num = input().split()
newnum = []
for i in range(len(num)):
    newnum.append(int(num[i]))
newnum.sort()
for i in range(len(newnum)):
    print(newnum[i])
print("")
for i in range(len(num)):
    print(num[i])