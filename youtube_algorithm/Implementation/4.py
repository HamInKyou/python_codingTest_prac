import sys;
input = sys.stdin.readline;

providedStr = input().rstrip();
alphabetList = [];
resultNum = 0;
for c in providedStr:
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
        resultNum += int(c);
    else:
        alphabetList.append(c);
alphabetList.sort();

if resultNum > 0:
    print("".join(alphabetList) + str(resultNum));
else:
    print("".join(alphabetList))


#c.isalpha()라는 메소드도 있다. 알파벳이면 true 리턴