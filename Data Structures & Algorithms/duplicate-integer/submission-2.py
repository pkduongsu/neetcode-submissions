class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert it into a set, and see if the len changes (less than the original) -> duplicate
        nums_set = set(nums)
        if (len(nums_set) < len(nums)):
            return True
        
        return False
         