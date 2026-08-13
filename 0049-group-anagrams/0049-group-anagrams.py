class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i])) # ex: aet
            if key in seen:
                seen[key].append(strs[i])
            else:
                seen[key] = [strs[i]]
        return list(seen.values())