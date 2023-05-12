# Tính S(n) = x + x^3 + x^5 + … + x^2n + 1
def bai14(x: int, n: int) -> int:
  sum=0
  for i in range(0,n):
      sum+=mypower(x,2*i+1)
  return sum

def mypower(x: int, n: int)->int:
  power=1
  for i in range(0,n):
      power*=x
  return power