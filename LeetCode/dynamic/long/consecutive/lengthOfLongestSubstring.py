def lengthOfLongestSubstring(s: str) -> int:

    vob = {}
    ans = 0
    i = -1
    for j in range(len(s)):
        if s[j] in vob:
            i = max(vob[s[j]], i)
        vob[s[j]] = j
        ans = max(j-i, ans)
    return ans


class Solution:
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))