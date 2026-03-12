class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        '''f[i]'''

        sp = " "+s
        f = [False] * (len(sp))
        f[0] = True

        for i in range(1,len(sp)):
            for j in wordDict:
                if(i - len(j)>=0):
                    if(j == sp[i+1-len(j): i+1]):
                        f[i] =  f[i] or (f[i-len(j)] and True)

        return f[len(sp)-1]
