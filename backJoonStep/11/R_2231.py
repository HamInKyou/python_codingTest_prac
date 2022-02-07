import sys;
input = sys.stdin.readline;

n = int(input());

minProducer = n;
for i in range(n, -1, -1):
    temp = i;
    divSum = temp;
    while temp > 0:
        divSum += temp % 10;
        temp = temp //10;        
    if divSum == n and i < minProducer:
        minProducer = i;

if minProducer < n:
    print(minProducer);
else:
    print(0)
        
