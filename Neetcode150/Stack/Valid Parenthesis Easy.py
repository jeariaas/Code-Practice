

def isValid(s: str) -> bool:

    dict = {"}": "{", "]":"[", ")":"("}
    stack = list()

    for letter in s:
        if letter not in dict:
            stack.append(letter)
            continue
        if not stack or stack[-1] != dict[letter]:
            return False
        stack.pop()
    return True

if isValid("[()]"):
    print(True)
else:
    print(False)