'''
rotate each element of list to its left
'''
def rotate_left3(nums):
  return (nums[1:]+nums[:1])


'''
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
'''
#max_end3([3, 11, 11]) → [11, 11, 11]
def max_end3(nums):
  if (nums[0]>nums[-1]):
    return [nums[0] for i in range(0,len(nums))]
  elif nums[0]<nums[-1]:
    return [nums[-1] for i in range(0,len(nums))]
  else:
    return [nums[0] for i in range(0,len(nums))]

'''
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
'''

def sum2(nums):
  if len(nums)==0:
    return 0;
  elif len(nums)<=2:
    return sum(nums);
  elif len(nums)>2:
    return (nums[0]+nums[1]);

def middle_way(a, b):
  l=[];
  l.append(a[1]);
  l.append(b[1]);
  return l;

'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
'''

'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

def count_evens(nums):
  l= [x for x in nums if x % 2 ==0]
  return len(l)

'''
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''


def sum13(nums):
  i = 0
  s = 0
  l=nums
  while (i < len(l)):
    if l[i] == 13:
      i += 2
    else:
      s += l[i]
      i += 1
  return s

'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''

def has22(nums):
    for x in range(len(nums)-1):
        if (nums[x] == 2) and (nums[x+1] == 2):
            return True
    return False


def has22_with_any(nums):
    l = nums;
    return (any(l[i] == 2 and l[i + 1] == 2 for i in range(len(l) - 1)))



if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8];
    print ('l[1:]->', l[1:]); # prints from second element to end
    print('l[:1]->', l[:1]);  # prints .. first element only
    print ('l in reverse order->', l[::-1]);
    print('each second element in list ->', l[::2]);
    print('each 3rd element in list ->', l[::3]);

    a=rotate_left3([1,2,3,4]);
    print (a);
    print (max_end3([3, 11, 11]));

    l= [10, 2];
    x=sorted(l);
    print(x[-1]-x[0])

    print(sum13([5, 13, 2]));

    print (has22_with_any([4, 2, 4, 2,  5]))