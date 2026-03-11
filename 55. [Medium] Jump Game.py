class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        step = 0
        loc = 0 
        while (loc <len(nums)-1 and nums[loc]!=0):
            next_loc = 0
            max_s = 0
            for j in range(0, nums[loc]+1):
                if(loc + j >= len(nums)-1):
                    next_loc = len(nums)-1
                    break
                elif( j+ nums[loc+j]>= max_s):
                    max_s = j + nums[loc+j]
                    next_loc = loc + j 
            step += 1
            loc = next_loc
        
        if(loc == len(nums)-1):
            ans =True
        else:
            ans =False 

        return ans
