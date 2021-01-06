# 上楼梯，共N阶楼梯。可以一次上一阶，也可以一次上两阶，上到第N阶有多少种方法
# 输入一个数字打印出“共xx种方法”和“程序用时xx秒”
import time

'''
加入缓存，避免重复计算
大体思路为先创建空缓存
其次遇到已经计算过的值，优先从缓存内读取
未计算过的值，算完之后存入缓存
基本可以瞬间算出结果，程序运行速度大大提高
'''
def stairs(n, cache=None):
	if cache is None:
		cache = {}
	if n in cache:
		return cache[n]
	if n == 1:
		cache[n] = 1
		return 1
	if n == 2:
		cache[n] = 2
		return 2
	if n >= 3:
		cache[n] = stairs(n-1, cache) + stairs(n-2, cache)
		return cache[n]

def test(n):
	print("台阶数：%d阶"%n)
	a = time.time()
	f = stairs(n)
	b = time.time()
	c = b - a
	print("共有%d种方法上楼"%f)
	print("解题耗时%f秒"%c)

if __name__ == '__main__':
	s = '''上楼梯，共N阶楼梯。可以一次上一阶，也可以一次上两阶，上到第N阶有多少种方法'''
	print(s)
	for i in range(50):
		test(i+1)

