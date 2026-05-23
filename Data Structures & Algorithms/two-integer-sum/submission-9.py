class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i in range(len(nums)):
            desired_value = target - nums[i]
            if desired_value in hashNum:
                return [hashNum[desired_value], i]
            else:
         
                hashNum[nums[i]] = i
                                    
        return []
