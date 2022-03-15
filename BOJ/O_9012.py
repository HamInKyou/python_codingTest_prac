import sys;
input = sys.stdin.readline;

t = int(input());

def parenthesisCheck(testString):
    stack = [];
    for c in testString:
        if c == "(":
            stack.append(c);
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop();
            else:
                return False;
    if len(stack) > 0:
        return False;
    else:
        return True;


for _ in range(t):
    stack = [];
    testCase = input().rstrip();
    if parenthesisCheck(testCase):
        print("YES");
    else:
        print("NO");