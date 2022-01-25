import sys;
input = sys.stdin.readline;

t = int(input());
for _ in range(t):
    x, y = map(int,input().split());
    distance = max(x,y) - min(x,y);
    energy = 0
    if distance <= 3:
        count = distance;
        distance = 0; 
    else:
        while energy**2 <= distance:
            energy+= 1;
        energy = energy - 1;
        distance -= energy**2;
        count = energy + energy-1;
    while distance > 0:
        if distance - energy >= 0:
            distance -= energy;
            energy -= 1;
            count += 1;
        else:
            energy -= 1;
    print(count)


