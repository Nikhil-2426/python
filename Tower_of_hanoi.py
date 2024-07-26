
def TowerOfHanoi(n, source, destination, intermediate):
   # print(n,source,destination,intermediate)
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    TowerOfHanoi(n-1, source, intermediate, destination)#(1,a,c,b)
    #
    # 
    # print(n,source,destination,intermediate)
    print(f"Move disk {n} from {source} to {destination}")
    TowerOfHanoi(n-1, intermediate, destination, source)


n = 5   
TowerOfHanoi(n, 'A', 'B', 'C')