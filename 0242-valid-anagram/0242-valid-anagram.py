class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {} # charecter --> their frequency
        seen_t = {}
        for i in range(len(s)):
            if s[i] in seen_s:
                seen_s[s[i]]+=1
            else:
                seen_s[s[i]]=1
        for j in range(len(t)):
            if t[j] in seen_t:
                seen_t[t[j]]+=1
            else:
                seen_t[t[j]]=1
        if seen_s == seen_t:
            return True
        return False

      
        