class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sp = ' '+s
        l = 0 
        r = 0
        flag = False
        for i in range(len(sp)-1,-1,-1):
            if(sp[i] != ' ' and not flag):
                flag = True 
                r = i
            elif(sp[i] == ' ' and flag):
                l = i
                break 


        return r-l
