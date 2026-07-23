class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return True

        s = s.strip()

        x = 0
        y = int(len(s) - 1)
        

        while (x < y):
            if (not s[x].isalnum()):
                x += 1
                continue

            if (not s[y].isalnum()):
                y -= 1
                continue

            if (s[x].lower() != s[y].lower()):
                return False

            x += 1
            y -= 1
            
        return True

            
