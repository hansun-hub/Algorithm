class Solution:
    def reverseVowels(self, s: str) -> str:
        # 문자열을 리스트로 변환하여 작업하기 편하게 만듭니다.
        s = list(s)
        
        # 모음을 저장할 리스트를 만듭니다.
        vowels = 'aeiouAEIOU'
        
        # 시작 인덱스와 끝 인덱스를 초기화합니다.
        start, end = 0, len(s) - 1
        
        while start < end:
            # 시작 인덱스에서 모음을 찾을 때까지 전진합니다.
            while start < end and s[start] not in vowels:
                start += 1
            
            # 끝 인덱스에서 모음을 찾을 때까지 후진합니다.
            while start < end and s[end] not in vowels:
                end -= 1
            
            # 모음을 서로 교환합니다.
            s[start], s[end] = s[end], s[start]
            
            # 시작과 끝 인덱스를 각각 이동합니다.
            start += 1
            end -= 1
        
        # 리스트를 다시 문자열로 변환하여 반환합니다.
        return ''.join(s)
