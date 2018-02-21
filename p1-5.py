def oneaway(str1, str2):
  failcount = 0
  if len(str1) == len(str2):
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        failcount +=1 

  elif len(str1) - len(str2) == 1:
    for i in range(len(str2)):
      if str1[i] != str2[i]:
        if str1[i+1] != str2[i]:
          failcount +=1    
  else:
    return False

  if failcount > 1:
    return False

  return True

print oneaway('pale', 'ple')

print oneaway('pales', 'pale')

print oneaway('pale', 'bale')

print oneaway('pale', 'bake')
