def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    
    left, right = 0, len(s)-1
    
    while left < right:
        if not s[left].isalpha():
            left+=1
        elif not s[right].isalpha():
            right -=1
        elif s[left].lower() == s[right].lower():
            left +=1
            right -=1
        else:
            return False
    return True

if __name__ == '__main__':
    s = input()
    res = is_palindrome(s)
    print('true' if res else 'false')