class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        answer = 0
        for i in range(k):
            if happiness[i] < i:
                return answer
            answer += happiness[i]
            answer -= i 
            
        return answer
