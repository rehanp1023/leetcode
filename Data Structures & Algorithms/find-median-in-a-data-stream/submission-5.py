class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array = sorted(self.array)

    def findMedian(self) -> float:
        arrlen = len(self.array)
        if arrlen == 0:
            return 0.0 
        if arrlen % 2 == 1:
            medianindex = (arrlen // 2)
            median = self.array[medianindex]
            return median   
        else: 
            medianindex1 = (arrlen // 2) 
            medianindex2 = (arrlen // 2) - 1
            median = float((self.array[medianindex1] + self.array[medianindex2]) / 2)
            return median