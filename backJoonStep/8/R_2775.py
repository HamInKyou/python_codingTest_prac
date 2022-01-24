import sys;
input = sys.stdin.readline;

testCase = int(input());

for _ in range(testCase):
    k = int(input());
    n = int(input());

    apartment = [[0]*(n+1) for _ in range(k+1)];
    #초기 아파트 세팅
    for i in range(1, n+1):
        apartment[0][i] = i;
    for j in range(k+1):
        apartment[j][1] = 1;
    #주민 집어넣기
    for x in range(1, k+1):
        for y in range(2,n+1):
            apartment[x][y] = apartment[x][y-1]+apartment[x-1][y];
    print(apartment[k][n])


    
