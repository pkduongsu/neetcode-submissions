class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: array of distinct integers nums, sorted in ascending order -> nums: List[int]
        #and an int: target
        #output: search for target within nums, if exists return index: int
        #else return -1

        #def search(nums: List[int], target: int) -> int
        l, r = 0, len(nums) - 1

        while l <= r:
            midPoint = (l + r) // 2
            if nums[midPoint] < target:
                l = midPoint + 1
            elif nums[midPoint] > target:
                r = midPoint - 1
            else:
                return midPoint

        return -1