'''Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid'''


class valid:
   def is_valid(self, s):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in char:
                stack.append(parenthese)
            elif len(stack) == 0 or char[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(valid().is_valid("(){}[]"))
print(valid().is_valid("()[{)}"))
print(valid().is_valid("()"))
