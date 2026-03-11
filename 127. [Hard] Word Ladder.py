class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Complexity O(N^2 L)
        Theoratical solvable, but sometimes need to opmize the constant 
        """
        
        if(endWord not in wordList):
            return 0
        
        def cmp(str1, str2):
            cnt_mismatch = 0
            for i in range(0,len(str1)):
                if(str1[i] != str2[i]):
                    cnt_mismatch += 1
                if(cnt_mismatch >1):
                    return False
            return True

        flag = [True] * len(wordList)

        q = deque()
        q.append([beginWord, 1])

        ans = 0

        while(q):
            temp = q.popleft()
            st = temp[0]
            step = temp[1]

            for i in range(0,len(wordList)):
                if(flag[i] and cmp(st,wordList[i])):
                    flag[i] = False
                    q.append([wordList[i], step+1])
                    if(wordList[i] == endWord):
                        ans = step+1
        

        return ans
