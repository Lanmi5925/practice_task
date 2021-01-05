# 动态规划题目
# n道菜，m元钱，刚好花完有多少种点餐方式
# 例如：
# 5道菜  分别售价【1,1,2,5,9,1】
# 共7元钱  可以有2种点餐方式

dish = int(input("共多少道菜："))
money = int(input("共多少钱："))
selling = []
for i in range(dish):
	a = int(input("第%d道菜价格："%(i+1)))
	selling.append(a)

way_list = [[0]*dish for i in range(money+1)]

print(way_list)
for i in range(1, dish):
	for j in range(1, money+1):
		# 如果当前售价大于手头钱数，则不取当前值
		if j < selling[i]:
			way_list[i][j]= way_list[i-1][j]
		# 如果当前售价小于或等于手头钱数，则取值
		else:
			way_list[i][j] = way_list[i-1][j] + way_list[i-1][j-selling[i]]

print(way_list[dish-1][money])