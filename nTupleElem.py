'''
4) Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
program:

# Input: Read the number of elements in the tuple
n = int(input())

# Input: Create a tuple by reading n elements from the user
elements = tuple(int(input()) for _ in range(n))

# Calculate the sum of the elements in the tuple
total_sum = sum(elements)

# Output: Print the sum of the tuple elements
print(total_sum)
'''
