class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        cnt1 = []
        cnt2 = []
        for i in range(len(words)):
            if words[i] == word1:
                cnt1.append(i)
            elif words[i] == word2:
                cnt2.append(i)
        res = 100000000
        len2 = len(cnt2)
        for item in cnt1:
            start = 0 
            end = len2-1
            mid = (start+end)//2
            while start<end:
                if cnt2[mid] < item:
                    start = mid + 1
                else:
                    end = mid
                mid = (start+end)//2
            if words[cnt2[mid]]==word2:
                res = min(res,abs(cnt2[mid]-item))
            if mid-1>-1 and words[cnt2[mid-1]]==word2:
                res = min(res,abs(cnt2[mid-1]-item))
        return res
