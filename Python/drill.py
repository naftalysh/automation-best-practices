"""
Given an array arr[] where each element represents the max number of steps that can be made forward from that index.

The task is to find the minimum number of jumps to reach the end of the array starting from index 0.

Examples:

    Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    Optional:
    Input: arr = [1, 3, 9, 5, 8, 2, 6, 7, 6, 8, 9]
    Output: 3 (1-> 3 -> 9 -> 9)
    Explanation: Jump from 1st element to 2nd element as there is only 1 step.
    Now there are three options 5, 8 or 9. If 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.

    Input:  arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Output: 10
    Explanation: In every step a jump is needed so the count of jumps is 10.

"""

# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
steps = 0


def getMaxJump(i):
    jumps = arr[i]
    ret_index = 0

    max_jumps = 0
    # for j in range(1, jumps):
    for j in range(1, jumps + 1):
        jump = arr[i + j]
        if max_jumps < jump + j:
            max_jumps = jump + j
            ret_index = i + j

    print(f"getMaxJump({i}) gets j={j}; max_jumps={max_jumps};ret_index={ret_index}")
    return ret_index


i = 0
while i < len(arr):
    val = arr[i]
    print(f"i = {i}; val = {val}")

    steps += 1
    print(f"steps={steps}")

    index = getMaxJump(i)
    print(f"index + arr[index] = {index + arr[index]}")

    if index + arr[index] >= len(arr):
        steps += 1
        print(f"num of steps = {steps}")

        break
    else:
        i = index
