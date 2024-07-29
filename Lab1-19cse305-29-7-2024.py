#!/usr/bin/env python
# coding: utf-8

# In[14]:


def count_pairs_with_sum(numbers, target_sum):
    pairs_count = 0
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs_count += 1
        seen.add(num)
    return pairs_count

def main():
    numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    target_sum = int(input("Enter the target sum: "))
    count = count_pairs_with_sum(numbers, target_sum)
    print(f"Number of pairs with sum equal to {target_sum}: {count}")

#main function
main()


# In[15]:


def calculate_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"
    
    min_val = numbers[0]
    max_val = numbers[0]
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return max_val - min_val

def main():
    numbers = list(map(float, input("Enter a list of real numbers separated by spaces: ").split()))
    result = calculate_range(numbers)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The range of the list is: {result}")

#main function
main()


# In[19]:


def matrix_mult(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(A, m):
    n = len(A)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    base = A
    while m > 0:
        if m % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        m //= 2
    
    return result

def main():
    n = int(input("Enter the size of the square matrix (n x n): "))
    print("Enter the matrix row by row, each row on a new line:")
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    m = int(input("Enter the power to which the matrix should be raised: "))
    result = matrix_power(matrix, m)
    print(f"Matrix raised to the power of {m} is:")
    for row in result:
        print(row)

#main function
main()


# In[20]:


def count_highest_occurring_char(input_string):
    count = {}
    
    for char in input_string:
        if char.isalpha():  # Consider only alphabets
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    
    if not count:
        return None, 0
    
    max_char = max(count, key=count.get)
    max_count = count[max_char]
    
    return max_char, max_count

def main():
    input_string = input("Enter a string: ")
    char, count = count_highest_occurring_char(input_string)
    if char is None:
        print("No alphabetic characters found.")
    else:
        print(f"Highest occurring character: '{char}' with count: {count}")

#main function
main()

