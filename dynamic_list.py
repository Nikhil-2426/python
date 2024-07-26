def pdct(x):
    product=1
    if len(x)==0:
        return "No Value"
    else:
        for i in x:
            product*=i
    return product        

int_list=[ 1,-1,2,3,4,-5]
print(int_list)
print(pdct(int_list))