class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_list = []
        for i, value in enumerate(nums):
            if value in new_list:
                new_list.remove(value)
            else:
                new_list.append(value)
        return new_list.pop()