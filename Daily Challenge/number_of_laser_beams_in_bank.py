from typing import List
def countOnes(row):
        count = 0
        for char in row:
            if char == '1':
                count += 1
        return count

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        for i in range (len(bank)):
            count = countOnes(bank[i])
            if count > 0:
                nextRow = i + 1
                while nextRow < len(bank) and countOnes(bank[nextRow]) == 0:
                    i += 1
                    nextRow = i + 1
                if nextRow < len(bank):
                    total = total + (count * countOnes(bank[nextRow]))
        return total