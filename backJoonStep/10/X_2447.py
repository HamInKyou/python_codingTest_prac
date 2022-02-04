import sys;
input = sys.stdin.readline;

def append_star(lenth): 
    if lenth == 1: 
        return ['*'] 
    
    prevPattern = append_star(lenth//3) #더 깊은 depth의 별 패턴 불러오기
    resultStars = [] 
    #더 깊은 depth의 별 패턴을 사용해서 새로운 패턴 만들기
    for stars in prevPattern: 
        resultStars.append(stars*3) 
    for stars in prevPattern: 
        resultStars.append(stars+' '*(lenth//3)+stars)
    for stars in prevPattern: 
        resultStars.append(stars*3) 
    #새로 만든 패턴 리턴
    return resultStars 
    
n = int(input()) 
print("\n".join(append_star(n)))
