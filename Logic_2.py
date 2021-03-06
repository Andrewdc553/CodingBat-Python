def make_bricks(small, big, goal):
"""
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""
    return (goal%5)<=small and (goal-(big*5))<=small

def lone_sum(a, b, c):
"""
Given 3 int values, a b c, return their sum. However,
if one of the values is the same as another of the values, it does not count towards the sum.
"""

  sum = 0
  sum +=a if a not in [b, c] else 0
  sum+=b if b not in [a, c] else 0
  sum += c if c not in [a, b] else 0 
  
  return sum  

# Our Solution:

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum


def lucky_sum(a, b, c):
"""
Given 3 int values, a b c, return their sum. However, 
if one of the values is 13 then it does not count towards the sum 
and values to its right do not count. So for example, if b is 13, then both b and c do not count.
"""
  list = [a, b, c, 13]
  sum = 0
  for n in list[:list.index(13)]:
    sum += n
  return sum  

def no_teen_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, 
    if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0,
    except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in 
    an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the 
    teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
    """
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  return n if n not in [13, 14, 17, 18, 19] else 0
