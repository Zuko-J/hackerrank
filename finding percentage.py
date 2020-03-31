def constraint_check(item):
    for x in item:
        if x >= 0 and x <= 100:
            check= True
        else:
            check= False
            break
    return check
def percent(n):
    d={}
    for y in range(n):
        name, *num= input().split()
        score= list(map(float, num))
    
        if constraint_check(score)== True:
            d[name.title()]=score
            
    namee=input().title()
    if namee in d.keys():
        z= sum(d[namee])/len(d[namee])
        print("{:.2f}".format(z))
        
n=int(input())
if n in range(2,11):
    percent(n)
