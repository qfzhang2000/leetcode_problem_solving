class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if(sum(nums) < target):
            return 0 
        
        l = 0
        r = 0
        ans = len(nums)
        temp = 0

        while(True):
            if(temp < target):
                if(r>= len(nums)):
                    break
                temp += nums[r]
                r += 1  
            elif(temp >= target):
                ans = min(ans, r-l)
                temp = temp - nums[l]
                l += 1

        return ans


