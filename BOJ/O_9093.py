import sys;
input = sys.stdin.readline;

t = int(input());

for _ in range(t):
    sentence = list(input().split());
    resultSentence = [];
    for word in sentence:
        stack = [];
        reversedWord = [];
        for c in word:
            stack.append(c);
        while stack:
            reversedWord.append(stack.pop());
        resultSentence.append("".join(reversedWord));
    print(" ".join(resultSentence));