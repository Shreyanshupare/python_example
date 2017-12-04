l = [(2,3),(3,5),(7,9),(8,10)]

def method(l):
    print("hii")
    q=[]
    for i in range(0,m):
        temp = a[i]
        if (i%2==0):
            c=temp[0]
            q.append(c)
        else:
            d=temp[1]
            q.append(d)  
    s = len(q)
    e =[]
    for i in range(0,s,2):
        e.append(tuple(q[i],q[i+1]))
        print(e)


method(l)        
