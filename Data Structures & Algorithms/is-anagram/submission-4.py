class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            chars = []
            for i in s:
                chars.append(i)
            
            for j in t:
                if j in chars:
                    chars.remove(j)

            if not chars:
                return True
            else: return False

        return False