# Tính S(n) = x + x^2 + x^3 + … + x^n
def bai12(x: int,n: int)->int:
  power=1
  sum=0
  for i in range(1,n+1):
    power*=x
    sum+=power
  return sum