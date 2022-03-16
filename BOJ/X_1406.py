import sys;
input = sys.stdin.readline;

# 시간초과된 풀이방법
# editor = input().rstrip();
# cursor = len(editor);
# n = int(input());

# for _ in range(n):
#     order = list(input().split());
#     if order[0] == 'L' and cursor > 0:
#         cursor -= 1;
#     elif order[0] == 'D' and  cursor < len(editor):
#         cursor += 1;
#     elif order[0] == 'B' and cursor > 0:
#         editor = editor[:cursor-1] + editor[cursor:];
#         cursor -= 1;
#     elif order[0] == 'P':
#         editor = editor[:cursor] + order[1] + editor[cursor:];
#         cursor += 1;\
# print(editor)

leftStack = list(input().rstrip());
rightStack = [];
n = int(input());

for _ in range(n):
    order = input().split();
    if order[0] == 'L' and leftStack:
        rightStack.append(leftStack.pop());
    elif order[0] == 'D' and rightStack:
        leftStack.append(rightStack.pop());
    elif order[0] == 'B' and leftStack:
        leftStack.pop();
    elif order[0] == 'P':
        leftStack.append(order[1]);

result = leftStack + list(reversed(rightStack));
print("".join(result));