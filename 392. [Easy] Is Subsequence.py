class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        loc = 0

        for i in t:
            if(loc >= len(s)):
                return True
            if(s[loc] == i):
                loc += 1

        if(loc >= len(s)):
            return True

        return False
