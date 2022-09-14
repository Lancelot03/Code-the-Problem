# o(n) space complexity
def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c=Counter(nums)
        return [i for i,N in c.items() if N > n//3]
