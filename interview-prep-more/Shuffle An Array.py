class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> list[int]:
        return self.original

    def shuffle(self) -> list[int]:
        shuffled = self.nums[:]
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
