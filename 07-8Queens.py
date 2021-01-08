'''
八皇后问题：在N*N 的棋盘上放N 个皇后，使得她们不能相互攻击。两个皇后能相互
攻击当且仅当她们在同一行或同一列或同一条对角线上。假设现准备在8*8 的棋盘上放
置8 个皇后，共有_______种放置方法。
'''
'''
利用二维列表来存储所有的结果，
第一层列表内存储字符串“.Q..”，来表示皇后位置，n皇后，字符串长度就为n
第二层列表，存储所有第一层列表的可能，列表有多长即有多少种解法
'''
'''
二维列表attack存储是否可以放置皇后，0表示可以，1表示不行
二维列表queen存储皇后放置的位置，.表示没放置，Q表示放置了皇后
'''
'''
皇后的攻击范围，如皇后位置为（x，y）
则所有的攻击方向为
[(x-1, y-1)左上, (x, y-1)正上, (x+1, y-1)右上]
[(x-1, y)正左, (x, y)本体, (x+1, y)正右]
[(x-1, y+1)左下, (x, y+1)正下, (x+1, y+1)右下]
设置方向列表，(dx,dy)为攻击方向
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1] 
'''

import copy

def putQueen(x, y, attack):
	# 利用双层循环，标记所有能攻击到的位置
	# 次循环不断从皇后本体外围向n-1的距离延伸
	attack[x][y] = 1
	size = len(attack)
	for i in range(size):
		i = i + 1
		# 此循环遍历8个方向
		for j in range(8): # 此处的8位8个方向
			nx = x + i*dx[j]
			ny = y + i*dy[j]
			if nx>=0 and ny>=0 and nx<size and ny<size :
				attack[nx][ny] = 1

def backtrack(k, n, queen, attack, solve):
	if k == n :
		solve.append(queen)
		return solve

	for i in range(n): 
		if attack[k][i]==0 :
			# temp = attack # 备份attack 此处为错误写法；这里是个坑，需要规避浅复制，不然attack列表无法重置
			temp = copy.deepcopy(attack)
			queen[k][i] = "Q"
			# print(queen)
			putQueen(k, i, attack)
			backtrack(k+1, n, queen, attack, solve)
			attack = copy.deepcopy(temp)
			queen[k][i] = "."


if __name__ == '__main__':
	n = int(input("请输入N皇后的N值："))
	attack = [[0 for i in range(n)] for i in range(n)]
	queen = [["." for i in range(n)] for i in range(n)]
	solve = []
	# 除去皇后本体（0,0），共8个方向
	dx = [-1,-1,-1,0,0,1,1,1]
	dy = [-1,0,1,-1,1,-1,0,1]
	backtrack(0, n, queen, attack, solve)
	print(len(solve))