from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            word = str(len(word)) + "#" + word 
            s += word
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            strs.append(word)
            i = j + 1 + length
        return strs