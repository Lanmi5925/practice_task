'''
有2*N 的长方形方格，用N 个1*2 的骨牌铺满方格，
现有12 个骨牌，共有_____种铺法。
'''
'''
思路：先确定最后一个骨牌的铺法
如果最后一块是竖直摆放，则f(N) = f(N-1)
如果最后一块是横向摆放，则f(N) = f(N-2)
所以最终f(N) = f(N-1) + f(N-2)
'''
def place_rect(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		f = place_rect(n-1) + place_rect(n-2)
		return f 

if __name__ == '__main__':
	# n = int(input("请输入骨牌个数："))
	for i in range(20):
		f = place_rect(i+1)
		print("共有%d种铺法"%f)