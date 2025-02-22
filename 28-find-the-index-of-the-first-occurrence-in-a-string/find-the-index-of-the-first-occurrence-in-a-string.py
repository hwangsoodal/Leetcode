class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        stop = len(haystack)
        return haystack.find(needle, start, stop)