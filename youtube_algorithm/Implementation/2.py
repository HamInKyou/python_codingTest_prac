import sys;
input = sys.stdin.readline;

n = int(input());

h = 0
m = 0
s = 0

cnt = 0
# while h <= n and m <= 59 and s <= 59:
#     s += 1;
#     if '3' in str(s) or '3' in str(m) or '3' in str(h):
#         cnt += 1;
#     if s == 60:
#         s = 0;
#         m += 1;
#     if m == 60:
#         m = 0;
#         h += 1;

# print(cnt);

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1;
print(cnt);