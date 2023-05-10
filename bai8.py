# Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2
def bai8(n: int)->int:
  sum=0
  for i in range(1,n+1):
    sum+=(2*i+1)/(2*i+2)
  return sum