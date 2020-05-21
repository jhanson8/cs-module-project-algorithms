'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''def single_number(arr):
    # Your code here
    return 2 * sum(set(arr)) - sum(arr)''' 



def single_number(nums):
    # keep track of the counts of how many times we've seen a particular number 
    # dictionaries are better at being searched 
    counts = {}

    #O(n)
    # loop through nums to tally up how many times we've seen each number 
    for x in nums:
        if x in counts: #O(1)
            del counts[x]
        else:
            counts[x] = 1

    # loop through all of the key-value pairs in counts to find the one pair
    # whose value is 1
    #O(1)
    for num in counts:
        if counts[num] == 1:
            return num



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")