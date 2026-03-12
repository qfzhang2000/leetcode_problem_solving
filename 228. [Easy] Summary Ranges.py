class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []

        if(nums is None or len(nums)==0):
            return []

        left = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] == cur+1 ):
                cur = cur + 1
            else:
                if(left != cur):
                    ans.append(str(left)+ "->" +  str(cur))
                else:
                    ans.append(str(left))
                left = nums[i]
                cur = nums[i]
        
        if(left != nums[-1]):
            ans.append(str(left)+ "->" +  str(nums[-1]))
        else:
            ans.append(str(left))

        return ans
