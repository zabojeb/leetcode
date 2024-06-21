class Solution:
    def calc(
        self, customers: List[int], grumpy: List[int], minutes: int, num: int
    ) -> int:
        ans = 0
        for i in range(minutes):
            if grumpy[i] == num:
                ans += customers[i]
        return ans

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        economy = self.calc(customers, grumpy, minutes, 1)

        max_economy = economy
        satisfied = self.calc(customers, grumpy, minutes, 0)
        for i in range(minutes, len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
            else:
                economy += customers[i]

            if grumpy[i - minutes] == 1:
                economy -= customers[i - minutes]

            if economy > max_economy:
                max_economy = economy

        return satisfied + max_economy
