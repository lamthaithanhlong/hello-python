# Bài 1: Tính S(n) = 1 + 2 + 3 + … + n
def bai1(n: int):
  sum=0
  for i in range(1,n+1):
    sum+=i;
  return sum