import time

ini = time.time()
ana1 = 'qwertyuioplkjhgfdsazxcvbnm'
ana2 = 'mnbvcxzqwertyuioplkjhgfdas'
ana1 = sorted(ana1)
ana2 = sorted(ana2)


def check(ana1,ana2):
    if ana1 == ana2:
        return True
    else:
        return False

c = check(ana1,ana2)
print(c)
fin = time.time()
print(fin-ini)