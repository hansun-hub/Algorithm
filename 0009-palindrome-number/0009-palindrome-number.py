class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        left =0
        right = len(tmp)-1

        while(left<=right):
            if tmp[left] != tmp[right]:
                return False
            else:
                left+=1
                right-=1
        return True