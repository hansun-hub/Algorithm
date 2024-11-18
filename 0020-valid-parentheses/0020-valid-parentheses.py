class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={']':'[','}':'{',')':'('}

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True