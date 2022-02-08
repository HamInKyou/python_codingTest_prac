import sys;
input = sys.stdin.readline;

n = int(input());
peopleList = []

for _ in range(n):
    personData = list(map(int, input().split()));
    peopleList.append(personData);

for personData in peopleList:
    count = 1;
    for anotherData in peopleList:
        if personData[0] < anotherData[0] and personData[1] < anotherData[1]:
            count += 1;
    print(count, end=" ")

