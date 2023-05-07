# Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n
def bai3(n: float):
  sum=0
  for i in range(1,n+1):
    sum+=1/i
  return sum