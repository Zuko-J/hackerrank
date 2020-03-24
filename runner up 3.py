n= int(input())
a= map(int, input().split())
p=[]
for x in a:
    if x >= -100 and x<=100 and n>=2 and n<=10 :
        p.append(x)
y=list(set(p))
y.sort()
print(y[-2])
