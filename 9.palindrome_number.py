class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 1
        n = str(x)
        for i in range(len(n)//2):
            if not n[i] == n[len(n)-1-i]:
                ans = 0
        return ans