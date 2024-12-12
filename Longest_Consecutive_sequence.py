# Longest Consecutive sequence:

# Given an unsorted array of integers 'nums', return the length of the longest consecutive element sequence.
# you must write an algorithm  that runs in 0(n) time.

# Example:

# Input: nums = [100,4,200,1,2,3]
# output: 4
# Explanation: The longest consecutive elements sequence is [1,2,3,4].
# Therefore its lenght is 4.

# Example:

# Input: nums =[0,3,7,2,5,8,4,6,0,1]
# output: 9  

def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            max_length = max(max_length, current_streak)

    return max_length

nums = []
print("Enter 6 random numbers in sequence and unsequence.")
for j in range(6):
  x=int(input())
  nums.append(x)

print(f"Therefore its lenght is: {longest_consecutive(nums)}")
