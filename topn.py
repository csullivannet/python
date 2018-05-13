#!/usr/bin/python

top = [0,0,0,0,0,0,0,0,0,0]

with open ("data.txt", "r") as f:
    for n in f:
        for i in range(10):
            if int(n) > top[i]:
                for j in range(9, i-1, -1):
                    if j == i:
                        top[j] = int(n)
                    else: 
                        top[j] = top[j-1]
                break

print top
