#Insertion sort in python
import time

def insertionSort(enter):
	start = time.clock()
	for i in  range(1,len(enter)):
		current = enter[i]
		position = i;

		while(position>0 and enter[position-1]>current):
			enter[position]= enter[position-1]
			position = position-1

		enter[position]= current
	end = time.clock()-start
	print(end)
	return enter


