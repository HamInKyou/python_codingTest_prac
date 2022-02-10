import sys;
input = sys.stdin.readline;

n = int(input());
people = list(map(int,input().split()));
people.sort()

groupCount = 0;
memberCount = 0;
for fear in people:
    memberCount += 1;
    
    if memberCount >= fear:
        memberCount = 0;
        groupCount += 1;

print(groupCount);
