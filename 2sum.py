from collections import deque
def solve(n, nums, target):
    h={}
    for i,e in enumerate(nums):
        if target - e in h:
            return [h[target-e],i]
        h[e]=i

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	target = int(input())
	out = solve(n, nums, target)
	print(*out)
# second method 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        old_num={}
        for i in range(len(nums)):
            if old_num.get(target - nums[i]) is not None:
                return [old_num.get(target - nums[i]), i]
            else:
                old_num[nums[i]] = i
