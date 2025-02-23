N:int=int(input())
C:list[int]=list(map(int, input()))
Q:int=int(input())

#合計販売枚数
sell=0
#全種類販売数
z=0
#セット販売数
s=0
#セット販売数の最小値
min_s_C=1000000000
#全体の最小値
min_z_C=1000000000

#初期値を記録
for i in range(0, N):
    if i%2==0:
        min_s_C=min(C[i],min_s_C)
    else:
        min_z_C=min(C[i],min_z_C)

#クエリを受け取る
for _ in range(0, Q):
    query = list(map(int, input().split()))

    if query[0]==1:
        x=query[1]-1
        a=query[2]
    #カードxがa枚あれば売る
        if x%2==0:
            card_x=C[a]-s-z
        else:
            card_x=C[a]-z
        if card_x>=a:
            C[X]-=a
            sell+=a

            if i%2==0:
                min_s_C=min(C[x], min_s_C)
            else:
                min_z_C=min(C[x], min_z_C)
    
    elif query[0]==2:
        a=query[1]
        if min_s_C-s-z >=a:
            s+=a
    
    elif query[0]==3:
        a=query[1]

        if min(min_s_C-s-z,min_z_C-z)>=a:
            z+=a
for i in range(0,N):
    if i%2==0:
        sell+=s
sell+=z*N
print(sell)