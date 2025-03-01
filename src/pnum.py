def is_prime(n:int)->bool:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
if __name__=='__main__':
    ans=is_prime(120)
    print(ans)