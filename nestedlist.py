n= int(input())
x= []
d=[]
p=0
if n >=2 and n<=5:
    for stud in range(n):
        name= input()
        score= float(input())
        j= [name, score]
        x.append(j)

    for val in x:
        y= x[p][1]
        p+=1
        d.append(y)
    
    z=list(set(d))
    x.sort()
    z.sort()

    for items in x:
        if z[1] in items:
            print(items[0])


    
    
