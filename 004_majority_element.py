def majority_element(self, nums):
    array_size = len(nums)//2

    for num in nums:
        qty = sum(1 for elem in nums if elem == num)
        if (qty == array_size):
            return 
