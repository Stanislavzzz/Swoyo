nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(nums)

print(nums[2:10]) # start stop step=1
print(nums[2:10:2]) # start stop step=1
print(nums[:15:2]) # start=0 stop step=1
print(nums[2::3]) # start stop=end step=1
print(nums[::-2]) # start stop=end step=1
print(nums[::-1]) # start stop=end step=1

new_list = nums[::-1]

print(nums)
print(new_list)
