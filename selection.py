#Selection sort in python
import time

def selectionSort(enter):
	start = time.clock()
	for i in  range(len(enter)):
		position = i
		for j in range(i+1,len(enter)):
			if (enter[position]>enter[j]):
				position = j
		swap(enter,position,i)
	end = time.clock()-start
	print(end)
	return enter

def swap(alist,position,i):
	alist[position],alist[i]=alist[i],alist[position]


