class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        inverse = defaultdict(list)
        heap = []
        output = []
        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key in hashmap:
            inverse[hashmap[key]].append(key)
            heap.append(-(hashmap[key]))

        heapq.heapify(heap)

        for i in range(k):
            frequency = abs(heapq.heappop(heap))
            frequentval = inverse[frequency].pop()
            output.append(frequentval)
        
        return output


        