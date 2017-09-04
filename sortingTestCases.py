import unittest
from bubble import bubbleSort
from selection import selectionSort
from insertion import insertionSort

class TestCases(unittest.TestCase):

	def testBubbleSort(self):

		self.assertEqual(bubbleSort([2,65,12,35,78,95,15,4]),[2,4,12,15,35,65,78,95])
		self.assertEqual(bubbleSort([1,5,9,12,56,89,94,102]),[1,5,9,12,56,89,94,102])
		self.assertEqual(bubbleSort([2,2,2,2,2,2,2,2,2,2]),[2,2,2,2,2,2,2,2,2,2])
		self.assertEqual(bubbleSort([]),[])
		self.assertEqual(bubbleSort([100,25]),[25,100])
		self.assertEqual(bubbleSort([2]),[2])
		self.assertEqual(bubbleSort([3,5,6,84,21,65]),[3,5,6,21,65,84])
		self.assertEqual(bubbleSort([3,5,6,21,65]),[3,5,6,21,65])

	def testInsertionSort(self):
		
		self.assertEqual(insertionSort([2,65,12,35,78,95,15,4]),[2,4,12,15,35,65,78,95])
		self.assertEqual(insertionSort([1,5,9,12,56,89,94,102]),[1,5,9,12,56,89,94,102])
		self.assertEqual(insertionSort([2,2,2,2,2,2,2,2,2,2]),[2,2,2,2,2,2,2,2,2,2])
		self.assertEqual(insertionSort([]),[])
		self.assertEqual(insertionSort([100,25]),[25,100])
		self.assertEqual(insertionSort([2]),[2])
		self.assertEqual(insertionSort([3,5,6,84,21,65]),[3,5,6,21,65,84])
		self.assertEqual(insertionSort([3,5,6,21,65]),[3,5,6,21,65])

	def testSelectionSort(self):
	
		self.assertEqual(selectionSort([2,65,12,35,78,95,15,4]),[2,4,12,15,35,65,78,95])
		self.assertEqual(selectionSort([1,5,9,12,56,89,94,102]),[1,5,9,12,56,89,94,102])
		self.assertEqual(selectionSort([2,2,2,2,2,2,2,2,2,2]),[2,2,2,2,2,2,2,2,2,2])
		self.assertEqual(selectionSort([]),[])
		self.assertEqual(selectionSort([100,25]),[25,100])
		self.assertEqual(selectionSort([2]),[2])
		self.assertEqual(selectionSort([3,5,6,84,21,65]),[3,5,6,21,65,84])
		self.assertEqual(selectionSort([3,5,6,21,65]),[3,5,6,21,65])

if __name__=='__main__':
	unittest.main()
