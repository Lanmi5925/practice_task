"""
作为第8题的补充
先尝试写出全排列，然后再设定剪枝条件，完成素数环
假设元素个数为n，求元素排列R的所有情况
当n=1时，P(R)=[r] r为排列中的唯一元素
当n>1时，P(R)=(r1)P(R1)+(r2)P(R2)+(r3)P(R3)+...+(rn)P(Rn)
其中Ri=R-{ri}。
即R的全排列等于先固定第一元素，剩下元素的全排列；加上固定第二元素，剩下元素的全排列；一直加到最后一个
"""
import copy


def backtrack(R, visted, path, depth, solve):
	if depth == len(R):
		solve.append(copy.deepcopy(path))  # 递归内的path列表会不断变化，因此不能直接将path添加进solve内，需要深度拷贝
		return
	for i in range(len(R)):  # 挨个拿列表内的元素
		if not visted[i]:
			visted[i] = True
			path.append(R[i])  # 当前元素没有被拿出来过，就把他加入到新列表里
			backtrack(R, visted, path, depth + 1, solve)  # 放入了上一元素之后，紧接着递归下一深度
			visted[i] = False  # 将元素状态还原
			path.pop()


if __name__ == '__main__':
	R = [1, 2, 3, 4]
	visted = [False for i in range(len(R))]
	path = []
	depth = 0
	solve = []
	backtrack(R, visted, path, depth, solve)
	print(len(solve))
	for i in solve:
		print(i, end="\n")
