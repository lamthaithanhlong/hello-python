# Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1
def bai7(n: int)->int:
  sum=0
  for i in range(0,n):
    sum+=(i+1)/(i+2)
  return sum