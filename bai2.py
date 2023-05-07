# Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2
def bai2(n: int):
  sum=0
  for i in range(1,n+1):
    sum+=i*i
  return sum