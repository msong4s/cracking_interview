def compact(s):
  s = s.lower()
  d = {}
  for i in s:
    if i != ' ':
      if i in d:
        d[i] += 1
      else:
        d[i] = 1
  return d

def oddnumbers(d):
  oddcount = 0
  for i in d:
    if d[i] % 2 == 1:
      oddcount += 1
  if oddcount > 1:
    return False
  return True

first = compact('Tact Coa')
print first
print oddnumbers(first) 
