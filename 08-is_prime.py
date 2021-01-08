'''
素数环问题，1,2,3，。。。，n个数组成的圆环，相邻两数之和为素数
当n=10时，起点为1的素数环共有多少种？
思路：仍然利用回溯法，将1设为起点，不断尝试，成功即返回一个素数环
不成功即返回上一层继续尝试
'''
# 创建一个函数用来判断两数之和是否为素数
from math import sqrt
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def backtrack(k, pList, n):
	if pList == [] :
		solve.append(sList)
		return solve
	# 首先遍历当前子节点
	for i in range(2, n+1):
		
		k = k + i
		if isPrime(k):
			k = i
			sList.append(i)
			pList.remove(i)
			# print(sList)
			# print(pList)
			backtrack(k, pList, n)


n = 5
pList = [i for i in range(2, n+1)]
sList = [1]
solve = []
# print(pList)
backtrack(1, pList, n)
print(len(solve))
