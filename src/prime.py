
def determinP(n:int,p:int)->bool:
    '''
    入力された整数nが整数pで割れるかまたpを各桁に含むかを判定する
    '''
    if n%p==0:
        return True
    while n>0:
        if n%10==p:
            return True
        n/=10
    return False

if __name__=='__main__':
    n,p=list(map(int, input().split()))
    ans=determinP(n,p)
    print(ans)