from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ""
        plen = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > plen:
                    p = s[l:r+1]
                    plen = len(p)
                l=l-1
                r=r+1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > plen:
                    p = s[l:r+1]
                    plen = len(p)
                l=l-1
                r=r+1
        return p