# REVERSE A STRING

# string = 'iamakashmystery'
# def reverse(string):
#     if len(string) == 1:
#         return string
#     return string[len(string)-1] + reverse(string[:len(string)-1])

# print(reverse(string))


# PERMUTATIONS OF A STRING

s = 'abc'
f = ['a','b','c']
lis = []
def permu(s,f,lis):
    if not f:
        return lis
    if s[0] in f:
        print(s) 
        lis.append(s[0]+s[1:])
    return permu(s,f.pop(s[0]))
print(permu(s,f,lis))
    