class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            # shift each char by 1
            for ch in word:
                encoded += chr(ord(ch) + 1)
            encoded += "/"  # separator
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            new_word = ""
            # decode until separator
            while i < len(s) and s[i] != "/":
                decoded_char = chr(ord(s[i]) - 1)
                new_word += decoded_char
                i += 1
            decoded_strs.append(new_word)
            i += 1  # skip the separator "/"
        return decoded_strs
