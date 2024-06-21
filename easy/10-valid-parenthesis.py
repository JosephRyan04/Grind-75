from typing import List

def isValid(s: str) -> bool:
    queue = list()
    open = ['{', '[', '(']
    close = ['}',']',')']
    for i in range(len(s)):
        if s[i] in open:
            queue.append(s[i])
        elif s[i] in close:
            if len(queue) < 1:
                return False
            if (s[i] == close[0] and queue[-1] == open[0]) or (s[i] == close[1] and queue[-1] == open[1]) or (s[i] == close[2] and queue[-1] == open[2]):
                queue.pop()
            else:
                return False

    return len(queue) == 0


if __name__ == '__main__':
    print(isValid("(])"))
    print(isValid("({}[]{{}[{]})"))
    print(isValid("({}[]{{}[]})"))
    print(isValid("(())"))
    print(isValid("[[]]"))
    print(isValid("{{}}"))
