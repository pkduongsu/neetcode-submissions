class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: nums: List[int]
        #return length of longest consecutive sequence that can be formed -> output: int
        #def LongestConsecutive(nums: List[int]) -> int
        
        #brute: for each number, find the longest possible consecutive sequence that can be formed
        # for loop for each number in the input array
        # skip duplicates -> use a set

        #store all the unique numbers of the input array in a set

        maxLength = 0
        uniqueNums = set(nums)

        for num in nums:
            streak = 0
            current = num
            while current in uniqueNums:
                streak += 1
                current += 1 #check if there is a consecutive sequence of this number
                #if next number is not in the set, break
                #-> we'll loop through every possible sequence that can be formed with this number
            #after we break out, update the max length
            maxLength = max(maxLength, streak)
        return maxLength

         


        