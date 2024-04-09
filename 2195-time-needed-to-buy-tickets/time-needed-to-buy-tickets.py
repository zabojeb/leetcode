class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target_tickets = tickets[k]
        time_taken = 0
        
        for position, num_tickets in enumerate(tickets):
            time_taken += min(num_tickets, target_tickets) if position <= k else min(num_tickets, target_tickets - 1)
        
        return time_taken
