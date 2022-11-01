# --------- Exercise 1 ---------

def sum_to(n):

  print(n * (n + 1) // 2)

sum_to(6)
sum_to(10)



# --------- Exercise 2 ---------

def largest(nums):
  nums.sort()
  return nums [-1] 

print(largest ([0, 1, 4, 6, 7, 13]))



# --------- Exercise 3 ---------

def occurances(string1, string2):
  return string1.count(string2)

print(occurances("hello there", "hi"))
print(occurances("what is good?", "who are you?"))



# --------- Exercise 4 ---------
def product(*args):
  product = 1
  for arg in args:
    product += arg
  return product

print(product(-2, 7))
print(product(-1, 5))