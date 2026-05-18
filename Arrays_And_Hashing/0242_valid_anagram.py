class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smap = {}  # char -> frequency
        tmap = {}

        for i in s:
            if i in smap:
                smap[i] += 1
            else:
                smap[i] = 1

        for i in t:
            if i in tmap:
                tmap[i] += 1
            else:
                tmap[i] = 1

        return smap == tmap


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
