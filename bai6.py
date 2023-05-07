# Bài 6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)
def bai6(n: int)->int:
  sum=0
  for i in range(1,n+1):
    sum+=1/(i*(i+1))
  return sum