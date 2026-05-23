#solution 2: store visited values

# -> Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []

        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.append(nums[i])
            else:
                return True
        
        return False

