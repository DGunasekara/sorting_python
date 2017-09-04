#Bubble sort in python
import time

def bubbleSort(enter):
	
	start = time.clock()
	for i in  range(len(enter)):
		for j in range(len(enter)-i-1):
			if (enter[j]> enter[j+1]):
				swap(enter,j,j+1)
	end = time.clock()-start
	print(end)
	return enter

def swap(alist,position,i):
	alist[position],alist[i]=alist[i],alist[position]
