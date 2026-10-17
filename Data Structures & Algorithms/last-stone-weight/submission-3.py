import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-1*stone)

        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y-x))

        return -1*heapq.heappop(heap) if heap else 0
            


        