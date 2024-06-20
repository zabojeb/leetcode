class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            
            try:
                if flowerbed[i - 1] == 1 and i != 0:
                    continue
            except:
                pass

            try:
                if flowerbed[i + 1] == 1:
                    continue
            except:
                pass

            flowerbed[i] = 1
                        
            count += 1
            if count >= n:
                return True
                
        if count < n:
            return False
        return True