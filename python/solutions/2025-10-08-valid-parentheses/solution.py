class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hashmap ={
            ")" : "(",
            "}" : "{",
            "]" : "["
           }
        for p in s:
            if p in hashmap:
                if stack and stack[-1]==hashmap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False

            
        