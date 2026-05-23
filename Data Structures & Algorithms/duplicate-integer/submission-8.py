class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert it into a set, and see if the len changes (less than the original) -> duplicate
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
            if hashMap[nums[i]] > 1: return True
        
        return False

         