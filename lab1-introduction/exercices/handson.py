
# B. avg
# Given a list of numbers, return the average of the list.
# If numbers equal [10, 10, 15, 7], the return value should be 10.5
def avg(numbers):
  # +++your code here+++
  average = 0
  for number in numbers:
    average = average+number
  average = average/len(numbers)
  return average

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # +++your code here+++
  return (s[0:2]+s[len(s)-2:])

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # +++your code here+++
  return (b + " "+ a)

# B. uniq
# Given a list of objects (numbers, strings, booleans), return the same list without duplicates.
# If a = [1, True, "otter", "platypus", 1, 2, False, "otter"]
# the return value should be [1, True, "otter", "platypus", 2, False]
# Note that the order does not matter
def uniq(a):
  # +++your code here+++
  return list(set(a))

# B. merge
# Given two sorted list of numbers, return a sorted list with the elements of both lists.
# If a = [1, 5, 13, 14] and b = [2, 7, 8, 42]
# the return value should be [1, 2, 5, 7, 8, 13, 14, 42]
def merge(a, b):
  # +++your code here+++
  tempList = (a+b)
  tempList.sort()
  return tempList

def test_avg():
    assert avg([10, 10, 15, 7]) == 10.5

def test_both_ends():
    assert both_ends("spring") == "spng"

def test_mix_up():
    assert mix_up('mix','pod') == "pod mix"
    assert mix_up('dog', 'dinner') == 'dinner dog'

def test_uniq():
    assert set(uniq([1, True, "otter", "platypus", 1, 2, False, "otter"])) == set([False, 1, 2, 'otter', 'platypus'])

def test_merge():
    assert merge([1, 5, 13, 14],[2, 7, 8, 42]) == [1, 2, 5, 7, 8, 13, 14, 42]