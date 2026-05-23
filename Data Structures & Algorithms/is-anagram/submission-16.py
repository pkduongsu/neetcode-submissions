#solution 1:
#actually

#if the sorted version of the 2 strings are equal, return True, else False
# -> ensure that the number of characters are also the same
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True

        return False        