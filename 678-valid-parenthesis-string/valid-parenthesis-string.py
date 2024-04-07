class Solution:
    def checkValidString(self, s: str) -> bool:
        mins, maxs = 0, 0
        for char in s:
            if char == "(":
                mins += 1
                maxs += 1
            elif char == ")":
                mins -= 1
                maxs -=1
            else:
                mins -= 1
                maxs +=1
            
            if maxs < 0:
                return False
            if mins < 0:
                mins = 0
                
        return mins == 0