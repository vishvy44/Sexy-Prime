a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if i+6<=b:
        for j in range(2,i+6):
            if j<i:
                if i%j==0 or (i+6)%j==0:
                    break
            if j>=i:
                if (i+6)%j==0:
                    break
            if j==i+5:
                print(i,i+6)
                count=count+1
            
            
    else:
        break
print(count)
        
            
