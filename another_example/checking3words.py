LIST = ["a","a","a","b","b","a","b","b","b"]

# checking for Uniqueness in list
aa = set(LIST)
print(aa)

li = []
i = 0
j = 3

# Selecting 3 continues words is same
# if it is same then 1 will print otherwise 0
while(j <= len(LIST)):
    print(i, j)
    z = LIST[i:j]
    print("inside while")
    if(z[0] == z[1] == z[2]):
        print("inside if")
        i = i + 1
        j = j + 1
        li.append(1)
        
    else:
        print("inside else")
        i = i + 1
        j = j + 1
        li.append(0)
        

print(li)    
