#solution 2: use a hashmap

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #did not check edge case if length of them are equal
        if len(s) != len(t):
            return False

        charMapS, charMapT = {}, {}

        for i in range(len(s)):
            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            charMapT[t[i]] = charMapT.get(t[i], 0) + 1

        if charMapS == charMapT:
            return True

        return False

