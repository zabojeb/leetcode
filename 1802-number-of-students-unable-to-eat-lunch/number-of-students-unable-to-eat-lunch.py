from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        for sandwich in sandwiches:
            if sandwich in students_queue:
                while students_queue[0] != sandwich:
                    students_queue.rotate(-1)
                students_queue.popleft()
            else:
                return len(students_queue)
        
        return 0
