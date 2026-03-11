class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        sp = sorted(citations)
        idx = 0
        ans = 0

        for i in range(0,max(sp)+1):
            while (sp[idx] < i):
                idx += 1 
            
            g_number = len(sp) - idx
            if (g_number >= i):
                ans = i
            else:
                break

        return ans
