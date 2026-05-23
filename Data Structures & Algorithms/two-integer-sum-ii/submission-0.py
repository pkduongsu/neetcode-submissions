class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: sorted numbers - increasing: List[int], targegt: int
        #def twoSum(numbers: List[int], target: int)
        #return indics of 2 numbers so that they add up to the target
        #and index 1 < index 2 -> return List[int] : [index1, index2]
        #what will be the expected return when there is no solution? / more than 1 solution? 
        #-> can assume there will be one valid solution

        #must use o(1) additional space
        #because, say we use a hash map, it will be o(n)
        
        #hashMap solution is just gonna be using the difference
        hashMap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in hashMap:
                return [hashMap[diff] + 1, i + 1]
            hashMap[numbers[i]] = i 
        
        return []

