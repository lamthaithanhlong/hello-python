# Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)
def bai5(n: int)->int:
  sum=0
  for i in range(0,n):
    sum+=1/(2*i+1)
  return sum