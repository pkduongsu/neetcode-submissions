class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}

        for i in range(len(nums)):
            currentVal = nums[i]
            if currentVal in prevMap:
                return True
            else:
                prevMap[nums[i]] = i
        
        return False