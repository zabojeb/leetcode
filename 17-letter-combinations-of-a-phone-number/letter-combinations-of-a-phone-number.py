class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits == "":
            return []

        combinations = [""]
        for digit in digits:
            letters = dictionary[digit]
            new_combinations = []
            for letter in letters:
                for combination in combinations:
                    new_combinations.append(combination + letter)

            combinations = new_combinations

        return combinations
