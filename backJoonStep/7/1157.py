"""
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""

import sys;
input = sys.stdin.readline;

s = input().rstrip();
upperS = s.upper();

alphaCnt = {};
for c in upperS:
    if c in list(alphaCnt.keys()):
        alphaCnt[c] += 1;
    else:
        alphaCnt[c] = 1;

maxkey = "";
maxValue = 0;
maxCnt = 0;

for key, value in alphaCnt.items():
    if value > maxValue:
        maxValue = value;
        maxCnt = 0;
        maxkey = key;
    elif value == maxValue:
        maxCnt += 1;

result = maxkey if maxCnt == 0 else '?';
print(result);

# Another soloution
# word = input().rstrip().upper();
# char_list = list(set(word));
# cnt = [];

# for i in char_list:
#     count = word.count(i)
#     cnt.append(count);

# if cnt.count(max(cnt)) >= 2:
#     print("?");
# else:
#     print(char_list[(cnt.index(max(cnt)))]);