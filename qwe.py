#code

def numpair(s1,s2):
    count = 0
    s2.sort()
    for ele in s1:
        for i in range(len(s2)):
            if ele != s2[i]:
            
                if ele == 0:
                    break
                
                
                if ele>1:
                    if s2[i]>ele:
                        count+=(len(s2)-i)
                        break
                    
                if s2[i] == 1 and ele != 1:
                    count+=(s1.count(1))
                    
                if ele == 2 and (s2[i] == 3 or s2[i] == 4):
                    count-=1
                    
                if ele == 1:
                    count += s2.count(0)
                
                if ele == 3 and s2[i]==2:
                    count+=1
            continue
    print(count)


t = int(input())
for i in range(t):
    n = input().split()
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    numpair(s1,s2)