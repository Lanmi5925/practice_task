# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的中位数。
'''
题目要求时间复杂度为O(log(m+n))
思路一：归并两个数组，得到一个排好序的大数组，
再来找中位数，时间复杂度为O(m+n), 空间复杂度也为O(m+n)
思路二：直接从下标0开始比对两个数组的元素大小，数字小的，
下标加一继续比对，直到比对到中位数的位置。
时间复杂度任然为O(m+n)，空间复杂度为O(1)
'''
nums1 = [1, 3, 5, 7, 11, 21, 35]
nums2 = [2, 6, 9, 12, 15]
print('nums1:', end='')
print(nums1)
print('nums2:', end='')
print(nums2)
# 思路一,先合并
def merge_list(a, b):
    if not a:
        return b
    if not b:
        return a
    a_index = b_index = 0
    ret = []
    while a_index < len(a) and b_index < len(b):
        if a[a_index] <= b[b_index]:
            ret.append(a[a_index])
            a_index += 1
        else:
            ret.append(b[b_index])
            b_index += 1
    if a_index < len(a):
        ret.extend(a[a_index:])
    if b_index < len(b):
        ret.extend(b[b_index:])
    return ret

if __name__ == '__main__':
	nums = merge_list(nums1, nums2)
	print(nums)
	i = len(nums)
	if i==0:
		k=0
	if i==1:
		k=nums[0]
	if i>=2:
		if i%2==0:
			k = (nums[int(i/2-1)] + nums[int(i/2)])/2
		else:
			k = nums[int(i/2)]
	print(k)




