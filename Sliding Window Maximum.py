def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        maxWindow = []
        for key, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(key)
            if queue[0] == key - k:
                queue.popleft()
            if key >= k-1:
                maxWindow.append(nums[queue[0]])
        return maxWindow
