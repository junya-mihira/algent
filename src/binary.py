def binary(v:list[int],a:int)->int:
    left =-1
    right =len(v)
    
    while (right-left>1):
        mid=left+int((right-left)/2)
        if v[mid]>=a:
            right =mid
        else :
            left =mid
    return right

if __name__=='__main__':
    nums=list(range(10))
    ans=binary(nums,5)
    print(ans)
