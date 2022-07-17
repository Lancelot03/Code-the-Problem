t=int(input())
while t>0:
        N=int(input())
        xli=[]
        xsum=[]
        for x in range(1,N):
                y=N-x
                # print(x,y)
                xo=x^y
                xli.append(xo)
                xsum.append([x,y])
        # print(xsum)
                
        for i in range(len(xli)):

                if sum(xsum[i]) == 2*xli[i]:
                        print(xsum[i][0],xsum[i][1])
        else:
                print(-1,-1)

        t-=1
                        
