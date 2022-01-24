import sys;
input = sys.stdin.readline;

n = int(input());

#5키로짜리로 최대한 담아보기
kg5Bag = n//5;
lastWeight = n%5;
result = kg5Bag + lastWeight//3 if lastWeight % 3 == 0 else -1;

#5키로를 최대로 했을 때 3키로로 안맞아떨어지면, 5키로 줄이고 3키로 늘려보기
while result == -1 and kg5Bag > 0:
    kg5Bag -= 1;
    lastWeight += 5;
    result = kg5Bag + lastWeight//3 if lastWeight % 3 == 0 and kg5Bag >= 0 else -1;

#결과 출력
print(result);