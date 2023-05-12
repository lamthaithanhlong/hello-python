# Tính S(n) = x^2 + x^4 + … + x^2n
def bai13(x:int,n: int)->int:
  power=1
  sum=0
  for i in range(0,n):
    power*=2*x
    sum+=power
  return sum