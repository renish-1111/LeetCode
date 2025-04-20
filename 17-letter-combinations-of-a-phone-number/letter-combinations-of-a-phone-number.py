class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        def parm(digits,string):
            if not digits:
                res.append(string)
                return
            for ch in keyboard[digits[0]]:
                parm(digits[1:],string+ch)

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []


        if digits:
            parm(digits,"")
        else:
            return []
        
        return res
