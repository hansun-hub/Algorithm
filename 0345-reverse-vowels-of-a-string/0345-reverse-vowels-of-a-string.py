class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"  # 대소문자 모음 문자열

        # 문자열을 리스트로 변환하여 뒤집을 모음 문자들을 저장할 리스트를 생성
        s = list(s)
        vowel_list = [c for c in s if c in vowels][::-1]

        # 문자열을 순회하면서 모음을 뒤집은 리스트의 값으로 교체
        vowel_idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list[vowel_idx]
                vowel_idx += 1

        # 리스트를 문자열로 변환하여 반환
        return ''.join(s)
