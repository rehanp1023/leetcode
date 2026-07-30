class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(', 
                    ']' : '[',
                    '}' : '{'}
        
        for char in s:
            if char not in mapping and char not in mapping.values():
                return False
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                value = stack.pop()
                if mapping[char] != value:
                    return False

        if not stack:
            return True
        else:
            return False 