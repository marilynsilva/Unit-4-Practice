'''4.1.1.1
Understand
Find if a number is divisible by numbers other than 0 or 1.

Plan
Use a while loop to try to divide by each number starting with two up to half of the target number

Implement'''
# def is_prime(n):
#   if n % 2 == 0: 
#     return False
#   index = 3
#   while index <= (n**0.5):
#     if n % index == 0:
#       return False
#   return True
# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))

'''4.1.1.2
Understand: Flipping a list

Plan: Starting at the ends, flip the value at both pointers, then move both pointers one position inward, and repeat until the pointers meet in the middle.

Implement'''
# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1

#   while left < right:
#     lst[left], lst[right] = lst[right], lst[left]
#     left += 1
#     right -= 1

#   return lst

# a=[1, 2, 3, 4, 5]
# b=[5, 4, 3, 2, 1]
# print(reverse_list(a))
# print(reverse_list(b))

'''
Two pointer:
  Time complexity: 0(n)
  Space Complexity:0(1)
'''

'''
def reverse_list(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for item in range(len(lst)):
      lst[i] = reversed_lst[i]
    print(item)

Splice method:
  Time complexity: 0(n)
  Space complexity: 0(n)
'''

'''
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

Understand:
The function sort_list_by_parity()  moves the the even integers to the beginning of the list and leaves the odd integers to the end.

Plan:

Implement:
'''

def sort_array_by_parity(nums):
  left=0
  right= len(nums)-1
  while left<right:
    if nums[right]%2==0:
      nums[left], nums[right]= nums[right], nums[left]
    left+=1
    right-=1

  return nums
            
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
