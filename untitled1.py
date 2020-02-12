a = 'abc'

def permu(a,l,r):
    if l==r:
        print(a)    
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permu(a,l+1,r)
            a[l],a[i]=a[i],a[l]

print(permu(list(a),0,len(a)-1))
# def rec(target, coins, known):
#     min_coins = target
#     if target in coins:
#         known[target] = 1
#         return 1
#     elif known[target]>0:
#         return known[target]
#     else:
#         for i in [c for c in coins if c<= target]:
#             num_coins = 1 + rec(target-i, coins, known)
#             if num_coins<min_coins:
#                 min_coins = num_coins
#                 known[target] = min_coins
#     return num_coins

# known = [0]*(13)
# print(rec(12,[1,5,10],known))