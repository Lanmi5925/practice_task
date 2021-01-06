'''
八皇后问题：在N*N 的棋盘上放N 个皇后，使得她们不能相互攻击。两个皇后能相互
攻击当且仅当她们在同一行或同一列或同一条对角线上。假设现准备在8*8 的棋盘上放
置8 个皇后，共有_______种放置方法。
'''
'''
此题需要遍历出每一种情况是否可行，所以复杂度很高无法避免
1）从第一列开始，为皇后找到安全位置，然后跳到下一列
2）如果在第n列出现死胡同，如果该列为第一列，棋局失败，否则后退到上一列，在进行回溯
3）如果在第8列上找到了安全位置，则棋局成功。
假设先放置的皇后坐标为q(x, y), 后放置的为q(row, col)，满足以下任一情况则冲突：
1）x=row(在纵向不能有两个皇后)
2) y=col（横向）
3）col + row = y+x;（斜向正方向）
4) col - row = y-x;（斜向反方向）
'''
'''
用一个长度为8的整数列表即可，存储8个皇后的位置
因为不能同行同列同斜线，因此8个皇后一定处于不同的8行
此时即可利用列表索引值代表行数
利用列表里的值代表列数
比如，第3行5列的皇后表示为，qList[3]=5
'''

n = int(input("NxN的棋盘，请输入N的值："))
# 创建列表存储皇后坐标
qList = n*[0]
# 当放下一个皇后时，需要判断此皇后是否安全
def isSafe(col, row, qList):
	tempCol = 0
	while tempCol<col:
		tempRow = qList[tempCol]
		if tempRow == row: #此时处于同一行，冲突
			return False
		elif tempCol == col: #此时处于同一列，冲突
			return False
		elif tempRow - tempCol == row - col: #此时处于同一斜线，冲突
			return False
		elif tempRow + tempCol == row + col: #此时处于另一斜线，冲突
			return False
		tempCol += 1 #继续判断，直到此行之前的所有皇后的安全区域均测试安全
	return True
	
def PlaceQueen(qList, col):
	row = 0
	foundSafePos = False
	if col == 8:
		foundSafePos = True;
	else:
		while row<8 and foundSafePos != True:
			if isSafe(col, row, qList):
				qList[col] = row
				foundSafePos = PlaceQueen(qList, col+1)
				if foundSafePos != True:
					row+=1

