def bubble_sort(nums: list[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]


nums = [5, 4, 10, 7, 1, 100, -1, -20]
print(f"Nums: {nums}")
bubble_sort(nums)
print(f"Sorted nums: {nums}")