class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        masks = [1 << i for i in range(len(nums))]
        for i in range(1 << len(nums)):
            yield [ss for mask, ss in zip(masks, nums) if i & mask]