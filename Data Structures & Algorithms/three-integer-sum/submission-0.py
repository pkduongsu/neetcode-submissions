class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute: loop through every possible combinations

        #can not have duplicates -> use set()
        res =  set()
        nums.sort() #as triplets can have same numbers, but different orders
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        res.add(tuple([nums[i], nums[j], nums[k]]))

        return [list(i) for i in res]
