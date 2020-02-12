# # def compress(s):
# #     d = {}
# #     string=''
# #     for alpha in s:
# #         if alpha not in d:
# #             d[alpha] = 1
# #         else:
# #             d[alpha] += 1
# #     for key,pair in d.items():
# #         # string.join(key)
# #         # string.join(pair)
# #         string = string + str(key) + str(pair)
# #     return string


# # print(compress('AAAAAAABBBBBccccwww'))


# # def unique(s):
# #     present = []
# #     for alpha in s:
# #         if alpha not in present:
# #             present.append(alpha)    
# #         else:
# #             return False
# #     return True

# # print(unique('abcdeafgh'))

# import sys

# data = []
# n=100
# for i in range(n):
#     data.append(n)

# z = len(data)
# s = sys.getsizeof(data)

# print("The array data has {0:3d} elements and occupy {1:4d} size".format(z,s))


# def count_substring(string, sub_string):
#     cnt=0
#     for i in range(0,len(string)):
#         if sub_string in string[i:i+3]:
#             cnt+=1
#     return cnt

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)


# class Stack(object):
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)

# s=Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


# BALANCED PARENTHESIS CHECK
#
# def check(s):
#     parenthesis = set('[{()}]')
#     if len(s)%2 !=0:
#         return False
#     opening = set('{[(')
#     matching = set([('(',')'),('{','}'),('[',']')])
#     stack = []
#
#     for paren in s:
#         if paren in parenthesis:
#             if paren in opening:
#                 stack.append(paren)
#             else:
#                 if len(stack)==0:
#                     return False
#                 last_open = stack.pop()
#                 if (last_open,paren) not in matching:
#                     return False
#     return True
# print(check('(5+5)+10-5)*(3+6)'))

# def add(x,y):
#     while y!=0:
#         carry = x&y
#         x = x^y
#         y=carry<<1
#     return x
# print(add(2,3))

# code
