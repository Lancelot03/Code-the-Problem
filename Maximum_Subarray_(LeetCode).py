class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = maxSum = nums[0]

        for num in nums[1:]:
            currentMax = max(num, currentMax + num)
            maxSum = max(currentMax, maxSum)

        return maxSum
