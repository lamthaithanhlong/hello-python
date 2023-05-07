# Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n
def bai4(n: int)->int:
  sum=0
  for i in range(1,n+1):
    sum+=1/(2*i)
  return sum