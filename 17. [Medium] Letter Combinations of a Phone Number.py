class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dict_key = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        ans = []
        max_len  = len(digits)
        temp = ""

        def iter_loop(cur, temp):
            if(cur >= max_len):
                ans.append(temp)
            else:
                for i in dict_key[digits[cur]]:
                    iter_loop(cur+1,temp+i)
        
        iter_loop(0,'')

        return ans
