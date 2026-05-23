class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #better: hashmap 
        #I think the pattern for this is
        # we find the gap between the current number 
        # and the target 
        # and when the gap is actually another element in 
        # the nums input list, return the pair 
        # else return [] by default

        # dict key should be the gap to be look up?
        # actually it needs to be the index

        # Time complexity: O(n)
        #space complexity: O(1)

        pairs = {}

        for i in range(len(nums)):
            if nums[i] in pairs:
                return[pairs[nums[i]], i]
            gap = target - nums[i]
            pairs[gap] = i

        return []

