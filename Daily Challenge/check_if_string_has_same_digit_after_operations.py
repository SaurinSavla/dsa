class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if (len(s)==1):
            return True
        if (len(s) == 2):
            if s[0] == s[1]:
                return True
            else:
                return False
        new = ""
        for i in range (len(s)-1):
            temp = (int(s[i]) + int(s[i+1])) % 10
            new += str(temp)

        if new == s:
            return False
        return self.hasSameDigits(new)