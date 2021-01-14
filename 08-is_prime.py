'''
素数环问题，1,2,3，。。。，n个数组成的圆环，相邻两数之和为素数
当n=10时，起点为1的素数环共有多少种？
思路：仍然利用回溯法，将1设为起点，不断尝试，成功即返回一个素数环
不成功即返回上一层继续尝试
'''
import copy
# 创建一个函数用来判断两数之和是否为素数
from math import sqrt


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def notR(i, a):
    if i in a:
        return False
    else:
        return True


def backtrack(pList, a, k, n, solve):
    if k == n:
        return solve.append(a)

    for i in pList:
        if notR(i, a):
            nsum = i + a[k - 1]
            if isPrime(nsum):
                print(i)
                a[k] = i
                backtrack(pList, a, k + 1, n, solve)


n = 5
pList = [i for i in range(1, n + 1)]
a = [0 for i in range(n)]
solve = []
a[0] = 1
backtrack(pList, a, 1, n, solve)
print(solve)
