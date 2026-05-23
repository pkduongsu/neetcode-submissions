class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert it into a set, and see if the len changes (less than the original) -> duplicate
        numSet = set(nums)
        if len(numSet) != len(nums):
            return True
        
        return False

         