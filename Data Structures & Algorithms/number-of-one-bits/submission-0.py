class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)

        count = 0

        for s in num:
            print(s)
            if (not (s.isalpha()) and int(s) == 1):
                count += 1
            
        return count