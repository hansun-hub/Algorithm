class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # 꽃을 심은 횟수를 저장할 변수

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # 현재 위치에 꽃을 심을 수 있는지 확인
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # 꽃을 심는다
                    count += 1  # 꽃을 심은 횟수를 증가

        # 꽃을 n개 심었으면 True를 반환, 아니면 False를 반환
        return count >= n