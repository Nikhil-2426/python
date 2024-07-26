lst=[1,2,3,6,4,5,7]
even=0
odd=0
for i in range(len(lst)):
    if lst[i]%2==0:
        even+=1
    else:
        odd+=1
print("N0 of even elements:",even)
print("No of odd elements:",odd)        
