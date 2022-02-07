import sys;
from itertools import combinations;

input = sys.stdin.readline;
n, m = map(int, input().split());
cards = list(map(int, input().split()));

max = 0;
cardCombination = list(map(list, combinations(cards,3)));
for choosedCard in cardCombination:
    totalNum = sum(choosedCard);
    if totalNum <= m and totalNum > max:
        max = totalNum;

print(max);



