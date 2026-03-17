class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        _dict = {}

        for i in range(0,len(s)):
            if((s[i] in _dict) and (_dict[s[i]] == t[i])):
                continue
            if(not (s[i] in _dict)):
                _dict[s[i]] = t[i]
                continue
            return False

        _d = {}
        for i in range(0,len(s)):
            if((t[i] in _d) and (_d[t[i]] == s[i])):
                continue
            if(not (t[i] in _d)):
                _d[t[i]] = s[i]
                continue
            return False


        return True



