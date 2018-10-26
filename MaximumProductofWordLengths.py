class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitMap = [0] * len(words)
        lens =[0] * len(words)
        res = 0
        def getBitMap(i, word):
            bits = 0
            for c in word:
                bits |= (1 << (ord(c) - ord('a')))
            lens[i] = len(word)
            bitMap[i] = bits
        for i in range(len(words)):
            if lens[i] == 0: getBitMap(i, words[i]);
            for j in range(i + 1, len(words)):
                if lens[j] == 0: getBitMap(j, words[j])
                if bitMap[i] & bitMap[j] == 0:
                    res = max(res, lens[i] * lens[j])
        return res
if __name__ == "__main__":
    s = Solution();
    words = ["abcw","baz","foo","bar","xtfn","abcdef"];
    print(s.maxProduct(words))
