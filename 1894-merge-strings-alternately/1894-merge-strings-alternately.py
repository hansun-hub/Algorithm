class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1=len(word1)
        length2=len(word2)
        i=0
        j=0
        res=""
        while i+j<length1+length2:
            if i<length1:
                res+=word1[i]
                i+=1
            if j<length2:
                res+=word2[j]
                j+=1
        return res