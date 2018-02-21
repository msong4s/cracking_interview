import sys

def replace(str, length):
  nstr = '' 
  i = 0
  while i < length:
    if str[i] == " ":
      nstr += "%20"
    else:
      nstr +=str[i]
    i+=1
  return nstr

s = "Mr John Smith    "
l = 13

print replace(s,l)
            
