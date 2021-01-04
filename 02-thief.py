s = '''n件藏品 每件有固定的重量和价值, 小偷的背包容量为m, 求小偷能偷的最大价值是多少'''
# 解题思路为：利用二维空间存储数据，避免重复计算，节省时间

max_w = int(input("背包最大容量："))
num = int(input("宝石数量:"))
weight_list = []
value_list = []
# 创建二维列表，用来存储每种情况的最优解
myList = [[0] * max_w for i in range(num)]
for i in range(num):
	a, b = input("输入重量和价值（用空格隔开）").split(" ")
	weight_list.append(int(a))
	value_list.append(int(b))

def ListValue(i, j):
	if i > 0:
		myList[i][j] = myList[i-1][j]
	else:
		myList[i][j] = 0

for i in range(num):
	for w in range(1, max_w+1):
		j = w - 1
		if w<weight_list[i]:
			ListValue(i, j)
		else:
			myList[i][j] = max(myList[i-1][j], myList[i-1][j-weight_list[i]]+value_list[i])

print(myList[num-1][max_w-1])