n, q = map(int, input().split())
car = list(map(int, input().split()))
car.sort()

for _ in range(q):
    i = int(input()) 
    if i in car:
        if i == car[0] or i == car[-1]:
            print(0)
        else:
            idx = car.index(i)
            c1 = idx
            c2 = len(car) - idx - 1
            print(c1*c2)
    else:
        print(0)
    