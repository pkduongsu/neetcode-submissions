class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if (diff not in prevMap): 
                #value/index/
                prevMap[nums[i]] = i 
            else: 
                return [prevMap[diff], i]

        return []
        
        