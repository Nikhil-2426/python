
def rhombus(n):
    for i in range(n):
        print(" "*i+" *"*n)


def invrhombus(n):
    for i in range(n):
        print(" "*(n-i-1)+"* "*n) 
    
        
    print("\n")    
def hollow(n):
    for i in range(n):
        if i==0 or i==n-1:
            print("* "*n)
        else:
            print("* "+"  "*(n-2)+"* ")

def pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i)+" *"*i)
    for i in range(1,n):
        print(" "*i+" *"*(n-i))
    print("\n")

def half_pyramid(n):
    for i in range(1,n):
        print(" *"*i)
    for i in range(n):
        print(" *"*(n-i))
    print("\n")







hollow(4)
print("==========================")
rhombus(4)
print("==========================")
invrhombus(4) 
print("==========================") 
pyramid(5)
half_pyramid(4)          