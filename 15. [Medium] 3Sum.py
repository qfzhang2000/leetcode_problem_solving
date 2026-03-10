class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        if n < 3:
            return ans

        sp = sorted(nums)

        for i in range(n - 2):
            if i > 0 and sp[i] == sp[i - 1]:
                continue
            if sp[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = sp[i] + sp[l] + sp[r]
                if s == 0:
                    ans.append([sp[i], sp[l], sp[r]])
                    l += 1
                    r -= 1

                    while l < r and sp[l] == sp[l - 1]:
                        l += 1
                    while l < r and sp[r] == sp[r + 1]:
                        r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ans
            
