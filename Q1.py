from typing import List
from  data_structures.heap import MaxHeap

def findKthLargest(nums: List[int], k) -> int:
	heap = MaxHeap.heapify(nums)
	for _ in range(k-1):
		heap.get_max()
	return heap.get_max()

if __name__ == "__main__":
	pass