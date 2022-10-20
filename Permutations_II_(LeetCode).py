class Solution:
    def permuteDfs(self, nums, visited, curr, ans):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            curr.append(nums[i])
            visited[i] = True
            self.permuteDfs(nums, visited, curr, ans)
            curr.pop()
            visited[i] = False
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return ans
        nums.sort()
        visited = [False]*len(nums)
        self.permuteDfs(nums, visited, [], ans)
        return ans
