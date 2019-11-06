def maxSubArray(self, nums):
    # for i in range(1, len(nums)):
    #     if nums[i-1] > 0:
    #         print(nums, nums[i], nums[i-1])
    #         nums[i] += nums[i-1]
    # return max(nums)

    # csum = msum = float("-inf")
    # for n in nums:
    #     csum = max(n, csum + n)
    #     msum = max(msum, csum)
    # return msum

    dp = [0] * len(nums) # dp[i] means the maximum subarray ending with A[i];
    max_ = dp[0] = nums[0]
    
    for i in range(len(nums)):
        dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0);
        # dp[i] = max(nums[i], nums[i]+dp[i-1])
        max_ = max(max_, dp[i])
    
    return max_