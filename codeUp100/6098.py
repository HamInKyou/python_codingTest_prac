"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

"""

MIROLENGTH = 10;
STARTPOSITION_X = 2;
STARTPOSITION_Y = 2;

miro = [];
for _ in range(MIROLENGTH):
    oneRow = input().split();
    miro.append(oneRow);

MoveToRight = True; #false면 아래로 이동
curPostionX = STARTPOSITION_X-1; #초기 개미 위치 설정
curPostionY = STARTPOSITION_Y-1; #초기 개미 위치 설정
while(True):
    #현재 위치 체크
    if miro[curPostionX][curPostionY] == '2': #먹이 있으면 체크하고 종료
        miro[curPostionX][curPostionY] = '9';
        break;
    
    #현재 위치 점령
    miro[curPostionX][curPostionY] = '9'
    
    #다음 위치 체크
    if MoveToRight:
        if miro[curPostionX][curPostionY+1] == '1': #오른쪽으로 가는 방향, 다음거 체크 (막혀있음 방향 비틀기, 재검사)
            MoveToRight = False;
            if miro[curPostionX+1][curPostionY] == '1': #아래로 가는 방향도 막혀있으면 종료
                break;
    else:
        if miro[curPostionX][curPostionY+1] != '1': #오른쪽으로 공간 생기면 방향 비틀기
            MoveToRight = True;
        else :
            if miro[curPostionX+1][curPostionY] == '1': #아래로 가는 방향, 다음거 체크 (막혀있음 종료)
                break;

    #다음 위치 이동
    if MoveToRight:
        curPostionY += 1;
    else:
        curPostionX += 1;

for oneRow in miro:
    print(" ".join(oneRow))
