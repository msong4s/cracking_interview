nnmatrix = [[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35]]

for line in nnmatrix:
  print line
print '--------------------'

def rotate90(mat):
  n = len(mat)
  if n%2 == 0:
    half = n/2
  else:
    half = int(n/2)+1

  r = 0 # row number
  for line in mat[0:half]:
    c = r # column number
    for v in line[r:n-1-r]:
      temp = mat[r][c]
      mat[r][c] = mat[n-1-c][r]
      mat[n-1-c][r] = mat[n-1-r][n-1-c]
      mat[n-1-r][n-1-c] = mat[c][n-1-r]   
      mat[c][n-1-r] = temp
      c+=1
    r+=1
  return mat

for line in rotate90(nnmatrix):
  print line

print '======================'
mmmatri = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
for line in mmmatri:
  print line
print '----------------------'
for line in rotate90(mmmatri):
  print line

