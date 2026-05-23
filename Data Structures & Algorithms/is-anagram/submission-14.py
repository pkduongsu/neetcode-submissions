class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input: string s, string t
        #output: bool: true if is anagram, not false

        #anagram: a string that has exact same characters as another string

        #def isAnagram(s: str, t: str) -> bool

        #easiest solution is just to check equality of the sorted strings
        #-> Time complexity depends on the complexity of sorting algo
        
        return sorted(s) == sorted(t)
        
    

            
        