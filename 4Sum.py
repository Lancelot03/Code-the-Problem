# def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         res, quad=[] , []
#         def kSum(k, start, target):
#             if k != 2:
#                 for i in range(start, len(nums)-k+1):
#                     if i > start and nums[i]==nums[i - 1]:
#                         continue
#                     quad.append(nums[i])
#                     kSum(k - 1, i + 1, target - nums[i])
#                     quad.pop()
#                 return
#             l, r = start, len(nums)-1
#             while l<r:
#                 if nums[l]+nums[r]<target:
#                     l+=1
#                 elif nums[l] + nums[r]>target:
#                     r -=1
#                 else:
#                     res.append(quad + [nums[l],nums[r]])
#                     l+=1
#                     while l<r and nums[l]== nums[l -1]:
#                         l+=1
        
#         kSum(4, 0, target)
#         return res

import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1
        return result
