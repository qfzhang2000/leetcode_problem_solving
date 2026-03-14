class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        dp = [[0 for _ in range(0,len(triangle))] for __ in range(0,len(triangle))]

        for i in range(0, len(triangle)):
            dp[len(triangle)-1][i] = triangle[len(triangle)-1][i] 

        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]
