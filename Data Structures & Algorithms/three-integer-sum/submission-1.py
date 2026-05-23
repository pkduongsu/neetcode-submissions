class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #better, O(n^2) solution:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #as nums is sorted, same values will stay near together
                continue
            
            #for each first value, we find the other 2 values using two pointers
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #as now the array is sorted, to reduce the sum value, go to smaller values towards left
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #update pointer -> shift the left pointer
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: #update the left pointer till its not the duplicate value, and maintain l < r ofc
                        l += 1

        return res

