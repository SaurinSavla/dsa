class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        if weeks:
            total = weeks * 28 + (7 * (weeks) * (weeks-1))//2
        else:
            total = 0
        monday = weeks + 1
        for i in range (1, (n % 7)+1):
            total += monday
            monday += 1
        return total