import sys

def com(s):
  former = ''
  nstr = ''
  count = 0
  for i in s:
    if i == former: # repeated character
      count += 1
    else:
      if count == 0: # first character
        former = i
        count = 1
      else:          # new character
        nstr += former
        nstr += str(count)
        former = i
        count = 1
  nstr += former
  nstr += str(count)
  return nstr

print com("aabcccccaaa")
print com("ggggggg")      
