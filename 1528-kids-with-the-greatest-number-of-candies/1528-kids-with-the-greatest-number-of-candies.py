class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        maxCandy=max(candies)
        for i in range(len(candies)):
            candy = candies[i]+extraCandies
            if candy>=maxCandy:
                output.append(True)
            else:
                output.append(False)
        return output