# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的中位数。
'''
题目要求时间复杂度为O(log(m+n))
思路一：归并两个数组，得到一个排好序的大数组，
再来找中位数，时间复杂度为O(m+n), 空间复杂度也为O(m+n)
思路二：直接从下标0开始比对两个数组的元素大小，数字小的，
下标加一继续比对，直到比对到中位数的位置。
时间复杂度任然为O(m+n)，空间复杂度为O(1)
思路三：暂时没思路
'''
nums1 = [1, 3, 5, 7, 11, 21, 35]
nums2 = [2, 6, 9, 12, 15]
print('nums1:', end='')
print(nums1)
print('nums2:', end='')
print(nums2)
# 思路二

n = len(nums1)+len(nums2)
if n==0:
	k=0
if n==1:
	if len(nums1)==0:
		k = nums2[0]
	else:
		k = nums1[0]
if n>=2:
	if n%2==0:
		i = int(n/2)
	else:
		i = int(n/2+1)




