from typing import List

def word_break(s: str, words: List[str]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return False

if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
