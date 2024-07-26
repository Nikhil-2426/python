
def rec(x):
    freqency={}
    for char in x:
        if char in freqency:
            freqency[char]+=1
        else:
            freqency[char]=1
        
    return freqency


str="banana"

result=rec(str)
print("Character frequncy")
print(result)