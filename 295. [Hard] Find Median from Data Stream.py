import heapq


class MedianFinder(object):

    def __init__(self):
        self.minq = [ 10e6]
        self.maxq = [ 10e6]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if (len(self.minq) == 0):
            heapq.heappush(self.minq,num)
        elif (len(self.maxq) == 0):
            heapq.heappush(self.maxq,-num)
        else:
            l_max = -self.maxq[0]
            r_min = self.minq[0]

            if(num<l_max):
                heapq.heappush(self.maxq,-num)
            else:
                heapq.heappush(self.minq,num)

            if(len(self.maxq)>len(self.minq)+1):
                temp = heapq.heappop(self.maxq)
                heapq.heappush(self.minq,-temp)
            elif(len(self.maxq)+1<len(self.minq)):
                temp = heapq.heappop(self.minq)
                heapq.heappush(self.maxq,-temp)        
        

    def findMedian(self):
        """
        :rtype: float
        """

        if (len(self.minq) == len(self.maxq)):
            l_max = -self.maxq[0]
            r_min = self.minq[0]
            return (float(l_max) + float(r_min))/2.0
        else:
            if(len(self.maxq)>len(self.minq)):
                return -self.maxq[0]
            else:
                return self.minq[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
