class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1
        
        arr = [[] for i in range(len(nums) + 1)]

        for n, c in countNums.items(): #return every key value pair in the countNums dict
            arr[c].append(n)

        res = []
        for i in range(len(arr) - 1, 0 , -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res

