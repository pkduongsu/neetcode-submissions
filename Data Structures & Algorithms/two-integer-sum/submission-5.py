class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #hashmap:
        #nums = [1, 2, 3, 4], target = 6 
        #nums[j] == target - nums[i] -> this (nums[j]) has to exist somewhere in the input array
        #Ex 1: nums[0] = 1 -> v = 6 - 1 = 5 -> if v in nums -> return its index as its what we were 
        #looking for -> using a hashmap that allows efficient lookups by keys, we can implement this
        #(key: desired value, value: index) -> hashNum[desired_value] == index -> return [i, hashNum[desired_value]]
        #Since this solution only goes through the input array once (worst case desired_value - index j will be at the end of the input array)
        #Time : O(n), Space: O(n), where n is the number of elements in the input array.

        hashNum = {}

        for i in range(len(nums)):       
            desired_val = target - nums[i]
            if desired_val in hashNum:
                return [hashNum[desired_val], i]
            else: 
                hashNum[nums[i]] = i

        return []   

