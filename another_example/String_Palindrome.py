def reverse(s): 
    return s[::-1] 
  
x = "malayalam is naman"
count=0
y = x.split(" ");
thisdict={};
w = "" 
for i in y[0:len(y)]:
  w=reverse(i)
  #print(w)
  if (i==w):
    #print("YES")
    thisdict[i]=++count
  	
print(thisdict)
