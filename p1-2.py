import sys

def permutation(str1,str2):

   if ''.join(sorted(str1)) == ''.join(sorted(str2)):
       return True

   return False

print permutation(sys.argv[1], sys.argv[2]) 
