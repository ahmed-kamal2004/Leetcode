class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:

            lista = []
            while x!=0:
                lista.append(x%10)
                x = x//10

            start = 0
            end = len(lista)-1

            while start !=end and end > start:
                if lista[start] != lista[end]:
                    return False
                start +=1
                end -=1

            return True

