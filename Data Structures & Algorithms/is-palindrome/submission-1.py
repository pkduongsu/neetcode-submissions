class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = []
        s_list = [char.lower() for char in s if char.isalnum()]
        print(s_list)
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                rev.append(s[i].lower())


        print(rev)

        return rev == s_list



