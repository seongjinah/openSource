#!/usr/bin/python

def union(l1, l2):
	return list(set(l1) | set(l2))

def intersection(l1, l2):
	return list(set(l1) & set(l2))
