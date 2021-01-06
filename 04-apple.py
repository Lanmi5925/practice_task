'''
把M 个同样的苹果放在N 个同样的盘子中，允许有的盘子空着不放苹果，
现有10 个苹果和7 个盘子，共有________种分法。
（说明：5,1,1 与1,5,1 代表同一种分法）
'''
'''
思路为先分析盘子与苹果数量的关系，
如果盘子多于苹果,if N>M
例如10个苹果放入15个盘子，那至少有5个盘子为空，
只需要考虑10个苹果放入10个盘子的情况。
也就是f(10,15)=f(10,10)
如果盘子数小于等于苹果数，if N<=M
则将所有放置的方法分为两类
一、所有盘子内都至少有一个苹果（以10苹果7盘子为例）
	那也就是说所有盘子均已有一个苹果，则只需要考虑剩余的苹果放法
	则f(10, 7) = f(3, 7)
二、至少有一个盘子是没放苹果的
	则f(10, 7) = f(10, 6)
所以f(10, 7) = f(3,7) + f(10, 6)
'''

def SortApple(m, n):
	if m==0 or n==1:
		return 1
	if m<n:
		f = SortApple(m, n-m)
		return f
	else:
		f = SortApple(m-n, n) + SortApple(m, n-1)
		return f

if __name__ == '__main__':
	m = int(input("请输入苹果数量:"))
	n = int(input("请输入盘子数量:"))
	f = SortApple(m, n)
	print("总共有%d种分类方法"%f)
