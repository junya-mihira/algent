def match(nums:list[int])->bool:
    s=nums[0]
    for i in nums[1::]:
        if i==s:
            return True
        s=i
if __name__=='__main__':
    nums=list(range(10))
    nums1=[0,1,2,3,4,5,5]
    ans=match(nums1)
    print(ans)
