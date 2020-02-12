#code
def nle(s):
    res = []
    res.append(s[0])

    for i in range(1,len(s)):
        next = s[i]    
        if res:
            a = res.pop(0)
            while a < next:
                print(next,end=' ')     
                if not res:
                    break
                a = res.pop(0)
            if a > next:
                res.append(a)
        res.append(next)
    while res:
        print(-1)
            
for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    nle(s)