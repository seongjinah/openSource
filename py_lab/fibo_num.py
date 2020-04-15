#!/usr/bin/python

n=int(input("fibonacci number? "))
f=[]

for i in range(n):
	if i<=1: f.append(1)
	else: f.append(f[i-1]+f[i-2])

for i in range(n-1):
	print(f[i], end=", ")


print(f[n-1])

print("F{}={}".format(n, f[n-1]))




