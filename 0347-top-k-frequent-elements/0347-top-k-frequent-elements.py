class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        input = Counter(nums)
        heap = []
        for num,freq in input.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k: heapq.heappop(heap)
        return [num for freq,num in heap]