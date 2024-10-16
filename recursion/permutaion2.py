def recur_permute(index, nums, ans):
    if index == len(nums):
        ans.append(nums[:])  # Create a copy of the current permutation
        return

    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        recur_permute(index + 1, nums, ans)
        nums[index], nums[i] = nums[i], nums[index]

nums = [1, 2, 3]
ans = []
recur_permute(0, nums, ans)
print(ans)
