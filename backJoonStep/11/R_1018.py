import sys;
input = sys.stdin.readline;

CHESSLEN = 8;
chessBoard = [];

def countChessColor (startX, startY, startColor):
    currentColor = startColor;
    count = 0
    for i in range(CHESSLEN):
            for j in range(CHESSLEN):
                if chessBoard[startX+i][startY+j] == currentColor:
                    count += 1;
                currentColor = 'B' if currentColor == 'W' else 'W';
            currentColor = 'B' if currentColor == 'W' else 'W';
    return count;

n,m = map(int, input().split());
for _ in range(n):
    row = input().rstrip();
    chessBoard.append(row);

resultArr = [];
for startX in range(n-CHESSLEN+1):
    for startY in range(m-CHESSLEN+1):
        resultArr.append(countChessColor(startX, startY, 'B'))
        resultArr.append(countChessColor(startX, startY, 'W'))

print(min(resultArr))