class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        step = 0
        loc = 0 
        while (loc <len(nums)-1):
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

        return step



        '''following is dp method'''

        # inf = int(10e9)
        # f = [inf for c in range(0,len(nums))]
        # f[0] = 0

        # for i in range(0,len(nums)-1):
        #     for j in range(0,nums[i]+1):
        #         if(i+j< len(nums)):
        #             f[i+j] = min(f[i+j], f[i]+1)
        
        # return f[len(nums)-1]


        
