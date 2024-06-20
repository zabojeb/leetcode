class Solution:
    def calc(self, arr):
        product = 1
        zero_found = False
        
        for num in arr:
            if num == 0:
                if not zero_found:
                    zero_found = True
                    continue
            product *= num
        
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = reduce(lambda x, y: x * y, nums)

        answer = []
        for num in nums:
            if num == 0:
                answer.append(self.calc(nums))
            else:
                answer.append(prod // num)
        
        return answer