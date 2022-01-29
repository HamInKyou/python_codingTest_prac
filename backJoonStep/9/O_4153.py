import sys;
input = sys.stdin.readline;

while True:
    edgeArr = list(map(int, input().split()));
    if edgeArr[0] == 0 and edgeArr[1] == 0 and edgeArr[2] == 0:
        break;
    edgeSquareArr = [x**2 for x in edgeArr];
    maxEdgeSquare = max(edgeSquareArr);
    if sum(edgeSquareArr) == 2*maxEdgeSquare:
        print("right");
    else:
        print("wrong")

