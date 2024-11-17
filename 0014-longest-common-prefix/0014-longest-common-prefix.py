class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: #빈 배열이면
        	return ''
        minStr = min(strs, key = len)
        for i, x in enumerate(minStr):
            for other in strs:
                if other[i] != x:
                	return minStr[:i]
        return minStr