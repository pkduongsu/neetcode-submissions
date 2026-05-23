#solution 1:
#use sorted, if they are equal -> equal length, equal chars 
#-> is Anagram, else false 

#time: based on the complexity of the sorting algorithm
#usually O(nlogn) with n being the length of input string (s, t)
#wrong: time: O(nlogn + mlogm) -> n, m being len of s, t
# space: O(2n) - wrong, O(n + m)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True 
        
        return False