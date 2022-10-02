
# def Write a Python program to square the 
# elements of a list using map() function.

def square_num(x):
  return x*x
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the list():")
print(list(result))