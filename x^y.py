#code

def numpair(s1,s2):
    count = 0
    s2.sort()
    for x in range(len(s1)):
        for y in range(len(s2)):
            if s2[y] == 0 and s1[x]!=0:
                count+=1
            if s1[x] ==2 and (s2[y] == 3 or s2[y] == 4):
                count-=1
            if s2[y] == 1 and s1[x]>1:
                count+=1
            if s1[x]>1 and s2[y]>1:
                if s1[x]<s2[y]:
                    count+=1
    print(count)


t = int(input())
for i in range(t):
    n = input().split()
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    numpair(s1,s2)