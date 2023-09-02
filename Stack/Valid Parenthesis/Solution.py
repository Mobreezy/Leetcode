import collections

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "]" : "[", "}" : "{"}
        stack = collections.deque()
        stack.append(s[0])
        for c in range(1, len(s)):
            if stack:
                if hashmap.get(s[c]) == stack[-1]:
                    stack.pop()
                elif s[c] in hashmap.values():
                    stack.append(s[c])
                else:
                    return False
            else:
                stack.append(s[c])
                
        if stack:
            return False
        else:
            return True