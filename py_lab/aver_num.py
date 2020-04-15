#!/usr/bin/python

N=int(input("How many numbers you want to calculate average?: "))

sum=0
for i in range(N):
	num=int(input("number {}: ".format(i+1)))
	sum=sum+num

ave=sum/N
print("average ", ave)












