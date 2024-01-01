class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x = str(x)
            start = 0
            while start!=len(x)-1-start and  len(x)-1-start> start:
                if x[start] != x[len(x)-1-start]:
                    return False
                else:
                    start+=1
            return True

