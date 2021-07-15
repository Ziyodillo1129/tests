# #Find the single element in a list where every element appears three times except for one.

def single_element(nums):
    ones, twos = 0, 0
    for x in nums:
        ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
    assert twos == 0
    return ones
nums1 = [5, 3, 4, 3, 5, 5, 3, 5, 4,]
nums2 = [-1, 1, 1, -1, -1, 1, 0, 4, 0, 0]
print(single_element(nums1))
print(single_element(nums2))

