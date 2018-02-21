import sys

def ifunique(st):
  temp = ""
  for i in st:
    if i in temp:
      return False
    temp += i

  return True

if ifunique(sys.argv[1]) == True:
  print "True"

else:
  print "False" 
