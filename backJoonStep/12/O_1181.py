import sys;
input = sys.stdin.readline;

n = int(input());

wordSet = set();
for _ in range(n):
    wordSet.add(input().rstrip());

wordArr = list(wordSet)
wordArr.sort(key = lambda x : (len(x),x));

for word in wordArr:
    print(word)