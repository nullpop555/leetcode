class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sn = sorted(nums, reverse=True)
        for i in range(len(sn)-2):
            a = sn[i:i+3]
            b = max(a)
            c = min(a)
            d = sum(a)
            if d > b * 2:
                return d
        return 0