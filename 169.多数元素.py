'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''


# def majorityElement(nums) -> int:
#     nums_set=sorted(list(set(nums)))
#     count=[0]*len(nums_set)
#     for i in nums:
#         count[nums_set.index(i)]+=1
#     return nums_set[count.index(max(count))]
# print (majorityElement([3,2,3,2,1,5,2]))

def majorityElement(nums) -> int:
    nums.sort()
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            if count > len(nums)/2:
                return (nums[i-1])
            else:
                count = 1
    return nums[-1]


print(majorityElement([-1, 1, 1, 1, 2, 1]))
