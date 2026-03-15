class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        sp = [[ None for _ in range(0,len(s)) ] for _ in range(0,numRows)]


        if(numRows == 1):
            return s

        loc = 1
        x1 = 0
        x2 = 0 
        sp[0][0] = s[0]
        while(loc<len(s)):
            for i in range(0,numRows -1):
                sp[x1+1][x2] = s[loc]
                x1 = x1 + 1 
                loc += 1
                if(loc>=len(s)):
                    break
            if(loc>=len(s)):
                    break
            for i in range(0,numRows -1):
                sp[x1-1][x2+1] = s[loc]
                x2 = x2 + 1 
                x1 = x1 - 1
                loc += 1
                if(loc>=len(s)):
                    break
        

        ans = ''
        for i in range(0, numRows):
            for j in range(0, len(s)):
                if(sp[i][j] is not None):
                    ans = ans + sp[i][j]
        
        return ans
